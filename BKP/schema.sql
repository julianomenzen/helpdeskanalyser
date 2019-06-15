--
-- PostgreSQL database dump
--

-- Dumped from database version 10.8 (Ubuntu 10.8-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.8 (Ubuntu 10.8-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_cas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_cas (
    id integer NOT NULL,
    user_id integer,
    created_on timestamp without time zone,
    service character varying(512),
    ticket character varying(512),
    renew character(1)
);


ALTER TABLE public.auth_cas OWNER TO postgres;

--
-- Name: auth_event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_event (
    id integer NOT NULL,
    time_stamp timestamp without time zone,
    client_ip character varying(512),
    user_id integer,
    origin character varying(512),
    description text
);


ALTER TABLE public.auth_event OWNER TO postgres;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    role character varying(512),
    description text
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_membership; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_membership (
    id integer NOT NULL,
    user_id integer,
    group_id integer
);


ALTER TABLE public.auth_membership OWNER TO postgres;

--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    group_id integer,
    name character varying(512),
    table_name character varying(512),
    record_id integer
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    first_name character varying(128),
    last_name character varying(128),
    email character varying(512),
    password character varying(512),
    registration_key character varying(512),
    reset_password_key character varying(512),
    registration_id character varying(512)
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: email; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.email (
    email_title character varying(512),
    email_text text,
    email_dataset_id integer,
    email_date date,
    email_user_id integer,
    id character varying NOT NULL
);


ALTER TABLE public.email OWNER TO postgres;

--
-- Name: email_feeling; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.email_feeling (
    feelingid character varying(36),
    id character varying(36) NOT NULL,
    probability numeric,
    emailid character varying(36)
);


ALTER TABLE public.email_feeling OWNER TO postgres;

--
-- Name: feeling; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.feeling (
    feeling_name character varying(512),
    id character varying(36)
);


ALTER TABLE public.feeling OWNER TO postgres;

--
-- Name: sender_email; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sender_email (
    id character varying NOT NULL,
    emailid character varying,
    email_sender character varying(512)
);


ALTER TABLE public.sender_email OWNER TO postgres;

--
-- Name: sender_to; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sender_to (
    id character varying NOT NULL,
    emailid character varying,
    email_to character varying(512)
);


ALTER TABLE public.sender_to OWNER TO postgres;

--
-- Name: consulta_bi; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.consulta_bi AS
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
   FROM ((((public.email
     LEFT JOIN public.sender_email ON (((email.id)::text = (sender_email.emailid)::text)))
     LEFT JOIN public.sender_to ON (((email.id)::text = (sender_to.emailid)::text)))
     LEFT JOIN public.email_feeling ON (((email.id)::text = (email_feeling.emailid)::text)))
     LEFT JOIN public.feeling ON (((email_feeling.feelingid)::text = (feeling.id)::text)));


ALTER TABLE public.consulta_bi OWNER TO postgres;

--
-- Name: dataset_emails; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dataset_emails (
    dataset_emailsid integer NOT NULL,
    dataset_emails character varying(512)
);


ALTER TABLE public.dataset_emails OWNER TO postgres;

--
-- Name: auth_cas auth_cas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_cas
    ADD CONSTRAINT auth_cas_pkey PRIMARY KEY (id);


--
-- Name: auth_event auth_event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_event
    ADD CONSTRAINT auth_event_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_membership auth_membership_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_membership
    ADD CONSTRAINT auth_membership_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: dataset_emails dataset_emails_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dataset_emails
    ADD CONSTRAINT dataset_emails_pkey PRIMARY KEY (dataset_emailsid);


--
-- Name: email_feeling email_feeling_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email_feeling
    ADD CONSTRAINT email_feeling_pkey PRIMARY KEY (id);


--
-- Name: email email_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.email
    ADD CONSTRAINT email_pkey PRIMARY KEY (id);


--
-- Name: sender_email sender_email_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sender_email
    ADD CONSTRAINT sender_email_pkey PRIMARY KEY (id);


--
-- Name: sender_to sender_to_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sender_to
    ADD CONSTRAINT sender_to_pkey PRIMARY KEY (id);


--
-- Name: auth_cas auth_cas_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_cas
    ADD CONSTRAINT auth_cas_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON DELETE CASCADE;


--
-- Name: auth_event auth_event_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_event
    ADD CONSTRAINT auth_event_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON DELETE CASCADE;


--
-- Name: auth_membership auth_membership_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_membership
    ADD CONSTRAINT auth_membership_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id) ON DELETE CASCADE;


--
-- Name: auth_membership auth_membership_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_membership
    ADD CONSTRAINT auth_membership_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON DELETE CASCADE;


--
-- Name: auth_permission auth_permission_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

