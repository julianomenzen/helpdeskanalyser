CREATE TABLE public.auth_cas
(
    id integer NOT NULL,
    user_id integer,
    created_on timestamp without time zone,
    service character varying(512) COLLATE pg_catalog."default",
    ticket character varying(512) COLLATE pg_catalog."default",
    renew character(1) COLLATE pg_catalog."default",
    CONSTRAINT auth_cas_pkey PRIMARY KEY (id),
    CONSTRAINT auth_cas_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.auth_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.auth_event
(
    id integer NOT NULL,
    time_stamp timestamp without time zone,
    client_ip character varying(512) COLLATE pg_catalog."default",
    user_id integer,
    origin character varying(512) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    CONSTRAINT auth_event_pkey PRIMARY KEY (id),
    CONSTRAINT auth_event_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.auth_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.auth_group
(
    id integer NOT NULL,
    role character varying(512) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    CONSTRAINT auth_group_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.auth_membership
(
    id integer NOT NULL,
    user_id integer,
    group_id integer,
    CONSTRAINT auth_membership_pkey PRIMARY KEY (id),
    CONSTRAINT auth_membership_group_id_fkey FOREIGN KEY (group_id)
        REFERENCES public.auth_group (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT auth_membership_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.auth_user (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.auth_permission
(
    id integer NOT NULL,
    group_id integer,
    name character varying(512) COLLATE pg_catalog."default",
    table_name character varying(512) COLLATE pg_catalog."default",
    record_id integer,
    CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
    CONSTRAINT auth_permission_group_id_fkey FOREIGN KEY (group_id)
        REFERENCES public.auth_group (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.auth_user
(
    id integer NOT NULL,
    first_name character varying(128) COLLATE pg_catalog."default",
    last_name character varying(128) COLLATE pg_catalog."default",
    email character varying(512) COLLATE pg_catalog."default",
    password character varying(512) COLLATE pg_catalog."default",
    registration_key character varying(512) COLLATE pg_catalog."default",
    reset_password_key character varying(512) COLLATE pg_catalog."default",
    registration_id character varying(512) COLLATE pg_catalog."default",
    CONSTRAINT auth_user_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.dataset_emails
(
    dataset_emailsid integer NOT NULL,
    dataset_emails character varying(512) COLLATE pg_catalog."default",
    CONSTRAINT dataset_emails_pkey PRIMARY KEY (dataset_emailsid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.dataset_training
(
    dataset_trainingid integer NOT NULL,
    dataset_textemail text COLLATE pg_catalog."default",
    dataset_feelingclasse character varying(50) COLLATE pg_catalog."default",
    dataset_feelingid integer
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.email
(
    email_title character varying(512) COLLATE pg_catalog."default",
    email_text text COLLATE pg_catalog."default",
    email_dataset_id integer,
    email_date date,
    email_user_id integer,
    id character varying COLLATE pg_catalog."default" NOT NULL,
    emailid integer NOT NULL DEFAULT nextval('email_emailid_seq'::regclass),
    CONSTRAINT email_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.email_feeling
(
    feelingid integer,
    id character varying(36) COLLATE pg_catalog."default" NOT NULL,
    probability numeric,
    emailid integer,
    email_feelingid integer NOT NULL DEFAULT nextval('email_feeling_email_feelingid_seq'::regclass),
    CONSTRAINT email_feeling_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.feeling
(
    feeling_name character varying(512) COLLATE pg_catalog."default",
    id character varying(36) COLLATE pg_catalog."default",
    feelingid integer NOT NULL DEFAULT nextval('feeling_feelingid_seq'::regclass)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.sender_email
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    emailid character varying COLLATE pg_catalog."default",
    email_sender character varying(512) COLLATE pg_catalog."default",
    CONSTRAINT sender_email_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE TABLE public.sender_to
(
    id character varying COLLATE pg_catalog."default" NOT NULL,
    emailid character varying COLLATE pg_catalog."default",
    email_to character varying(512) COLLATE pg_catalog."default",
    CONSTRAINT sender_to_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

CREATE OR REPLACE VIEW public.consulta_bi AS
 SELECT email.email_title,
    email.email_text,
    email.email_dataset_id,
    email.email_date,
    email.email_user_id,
    email.id,
    sender_email.id AS idsenderemail,
    sender_email.email_sender,
    sender_to.id AS idto,
    sender_to.email_to,
    email_feeling.probability,
    feeling.feeling_name,
    email_feeling.id AS idemailfeeling,
    feeling.id AS idfeeling
   FROM email
     LEFT JOIN sender_email ON email.id::text = sender_email.emailid::text
     LEFT JOIN sender_to ON email.id::text = sender_to.emailid::text
     LEFT JOIN email_feeling ON email.emailid = email_feeling.emailid
     LEFT JOIN feeling ON email_feeling.feelingid = feeling.feelingid;

