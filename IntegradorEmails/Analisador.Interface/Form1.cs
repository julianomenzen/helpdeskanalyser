using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using ActiveUp.Net.Mail;
using Npgsql;

namespace Analisador.Interface
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Valida os campos
            if (string.IsNullOrEmpty(txtEnderecoEmail.Text))
            {
                MessageBox.Show("O endereço de e-mail deve ser informado!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }

            if (string.IsNullOrEmpty(txtSenha.Text))
            {
                MessageBox.Show("A senha deve ser informada!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }

            if (string.IsNullOrEmpty(txtNomeCaixa.Text))
            {
                MessageBox.Show("O nome da caixa de e-mails deve ser informado!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }

            if (string.IsNullOrEmpty(txtQtdEmails.Text))
            {
                MessageBox.Show("A quantidade de e-mails a serem buscados deve ser informada!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }

            //Conecta na conta de e-mail informada
            var mailRepository = new MailRepository(
                           "imap.gmail.com",
                           993,
                           true,
                           txtEnderecoEmail.Text,
                           txtSenha.Text
                       );


            Mailbox mail = mailRepository.GetMailBox(txtNomeCaixa.Text);
            barraProgresso.Visible = true;
            barraProgresso.Minimum = 0;
            barraProgresso.Maximum = (mail.MessageCount + 1);
            barraProgresso.Value = 1;

            for (int n = 1; n < mail.MessageCount + 1; n++)
            {
                ActiveUp.Net.Mail.Message newMessage = mailRepository.GetMail(mail, n);
                InserirEmail(newMessage);
                barraProgresso.Value++;
                this.Refresh();
            }
            barraProgresso.Visible = false;
        }

        private void InserirEmail(ActiveUp.Net.Mail.Message mes)
        {
            string strConexao = ConfigurationManager.ConnectionStrings["conexao"].ToString();
            Guid IdEmail = Guid.NewGuid();

            using (NpgsqlConnection con = new NpgsqlConnection(strConexao))
            {
                con.Open();
                using (var trans = con.BeginTransaction())
                {
                    try
                    {
                        //Insere o e-mail
                        NpgsqlCommand cmd = new NpgsqlCommand();
                        cmd.Connection = con;
                        cmd.Transaction = trans;
                        cmd.CommandText = "insert into email (id, email_title, email_text, email_date ) values (@id, @email_title, @email_text, @email_date)";
                        cmd.Parameters.AddWithValue("id", IdEmail.ToString());
                        cmd.Parameters.AddWithValue("email_title", mes.Subject);
                        cmd.Parameters.AddWithValue("email_text", mes.BodyText.Text);
                        cmd.Parameters.AddWithValue("email_date", mes.Date);
                        cmd.ExecuteNonQuery();
                        cmd.Parameters.Clear();

                        //Insere o sender
                        cmd.CommandText = "insert into sender_email (id, emailid, email_sender) values (@id, @emailid, @email_sender)";
                        cmd.Parameters.AddWithValue("id", Guid.NewGuid().ToString());
                        cmd.Parameters.AddWithValue("emailid", IdEmail.ToString());
                        cmd.Parameters.AddWithValue("email_sender", mes.From.Email);
                        cmd.ExecuteNonQuery();
                        cmd.Parameters.Clear();

                        //Insere o To
                        foreach(var mail in mes.To)
                        {
                            cmd.CommandText = "insert into sender_to (id, emailid, email_to) values (@id, @emailid, @email_to)";
                            cmd.Parameters.AddWithValue("id", Guid.NewGuid().ToString());
                            cmd.Parameters.AddWithValue("emailid", IdEmail.ToString());
                            cmd.Parameters.AddWithValue("email_to", mail.Email);
                            cmd.ExecuteNonQuery();
                            cmd.Parameters.Clear();
                        }

                        trans.Commit();
                    }
                    catch (Exception e)
                    {
                        trans.Rollback();
                    }
                }
            }
        }
    }
}
