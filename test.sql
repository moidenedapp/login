--
-- PostgreSQL database dump
--

-- Dumped from database version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.22 (Ubuntu 12.22-0ubuntu0.20.04.1)

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
-- Name: base_cache_signaling_assets; Type: SEQUENCE; Schema: public; Owner: moises
--

CREATE SEQUENCE public.base_cache_signaling_assets
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_cache_signaling_assets OWNER TO moises;

--
-- Name: base_cache_signaling_default; Type: SEQUENCE; Schema: public; Owner: moises
--

CREATE SEQUENCE public.base_cache_signaling_default
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_cache_signaling_default OWNER TO moises;

--
-- Name: base_cache_signaling_groups; Type: SEQUENCE; Schema: public; Owner: moises
--

CREATE SEQUENCE public.base_cache_signaling_groups
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_cache_signaling_groups OWNER TO moises;

--
-- Name: base_cache_signaling_routing; Type: SEQUENCE; Schema: public; Owner: moises
--

CREATE SEQUENCE public.base_cache_signaling_routing
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_cache_signaling_routing OWNER TO moises;

--
-- Name: base_cache_signaling_templates; Type: SEQUENCE; Schema: public; Owner: moises
--

CREATE SEQUENCE public.base_cache_signaling_templates
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_cache_signaling_templates OWNER TO moises;

--
-- Name: base_registry_signaling; Type: SEQUENCE; Schema: public; Owner: moises
--

CREATE SEQUENCE public.base_registry_signaling
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.base_registry_signaling OWNER TO moises;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: modules; Type: TABLE; Schema: public; Owner: moises
--

CREATE TABLE public.modules (
    id integer NOT NULL,
    name character varying NOT NULL,
    created_at date,
    update_at date
);


ALTER TABLE public.modules OWNER TO moises;

--
-- Name: permissions; Type: TABLE; Schema: public; Owner: moises
--

CREATE TABLE public.permissions (
    id integer NOT NULL,
    role_id integer NOT NULL,
    module_id integer NOT NULL,
    can_read boolean,
    can_write boolean,
    can_delete boolean,
    can_update boolean
);


ALTER TABLE public.permissions OWNER TO moises;

--
-- Name: roles; Type: TABLE; Schema: public; Owner: moises
--

CREATE TABLE public.roles (
    name character varying NOT NULL,
    created_at date DEFAULT CURRENT_TIMESTAMP,
    update_at date DEFAULT CURRENT_TIMESTAMP,
    id integer NOT NULL
);


ALTER TABLE public.roles OWNER TO moises;

--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: moises
--

ALTER TABLE public.roles ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.roles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: users; Type: TABLE; Schema: public; Owner: moises
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying NOT NULL,
    lastname character varying NOT NULL,
    email character varying NOT NULL,
    created_at date DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at date DEFAULT CURRENT_TIMESTAMP NOT NULL,
    role_id integer NOT NULL
);


ALTER TABLE public.users OWNER TO moises;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: moises
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: modules; Type: TABLE DATA; Schema: public; Owner: moises
--

COPY public.modules (id, name, created_at, update_at) FROM stdin;
\.


--
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: moises
--

COPY public.permissions (id, role_id, module_id, can_read, can_write, can_delete, can_update) FROM stdin;
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: moises
--

COPY public.roles (name, created_at, update_at, id) FROM stdin;
administrator	2024-12-19	2024-12-19	2
supervisor_almacen	2024-12-19	2024-12-19	3
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: moises
--

COPY public.users (id, name, lastname, email, created_at, updated_at, role_id) FROM stdin;
4	Alex	Trejo	alex@trejo.com	2024-12-19	2024-12-19	2
6	Moisés	Rangel	moii@trejo.com	2024-12-19	2024-12-19	3
\.


--
-- Name: base_cache_signaling_assets; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.base_cache_signaling_assets', 1, true);


--
-- Name: base_cache_signaling_default; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.base_cache_signaling_default', 1, true);


--
-- Name: base_cache_signaling_groups; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.base_cache_signaling_groups', 1, true);


--
-- Name: base_cache_signaling_routing; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.base_cache_signaling_routing', 1, true);


--
-- Name: base_cache_signaling_templates; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.base_cache_signaling_templates', 1, true);


--
-- Name: base_registry_signaling; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.base_registry_signaling', 1, true);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.roles_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: moises
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


--
-- Name: modules modules_pk; Type: CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.modules
    ADD CONSTRAINT modules_pk PRIMARY KEY (id);


--
-- Name: modules modules_unique; Type: CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.modules
    ADD CONSTRAINT modules_unique UNIQUE (name);


--
-- Name: permissions permissions_pk; Type: CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pk PRIMARY KEY (id);


--
-- Name: roles roles_pk; Type: CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pk PRIMARY KEY (id);


--
-- Name: roles roles_unique; Type: CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_unique UNIQUE (name);


--
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- Name: users users_unique; Type: CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_unique UNIQUE (email);


--
-- Name: users_email_idx; Type: INDEX; Schema: public; Owner: moises
--

CREATE UNIQUE INDEX users_email_idx ON public.users USING btree (email);


--
-- Name: users users_roles_fk; Type: FK CONSTRAINT; Schema: public; Owner: moises
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_roles_fk FOREIGN KEY (role_id) REFERENCES public.roles(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

