PGDMP     2                    y           espresso    10.16 #   12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16384    espresso    DATABASE     x   CREATE DATABASE espresso WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';
    DROP DATABASE espresso;
                pgadmin    false            �          0    16572    beans_intake_location 
   TABLE DATA           =   COPY public.beans_intake_location (id, location) FROM stdin;
    public          pgadmin    false    219          �           0    0    beans_intake_location_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.beans_intake_location_id_seq', 4000003, true);
          public          pgadmin    false    218            �   K   x�31 N���T��Ҽ��̼b.��!�Wbnn)�g��^������_�Z\Sc����ZT�����R����� �S2     