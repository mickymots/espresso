PGDMP                         y           espresso    10.16 #   12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16384    espresso    DATABASE     x   CREATE DATABASE espresso WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';
    DROP DATABASE espresso;
                pgadmin    false            ?          0    16580    beans_intake_status 
   TABLE DATA           M   COPY public.beans_intake_status (id, status, status_description) FROM stdin;
    public          pgadmin    false    221   '       ?           0    0    beans_intake_status_id_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.beans_intake_status_id_seq', 3000003, true);
          public          pgadmin    false    220            ?   A   x?36 NO?GoW(?e4?t	???s?RPQ#? ???0???s89{???? X\1z\\\ ?v?     