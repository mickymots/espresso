PGDMP                         y           espresso    10.16 #   12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16384    espresso    DATABASE     x   CREATE DATABASE espresso WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';
    DROP DATABASE espresso;
                pgadmin    false            �          0    16553    beans_intake_employee 
   TABLE DATA           f   COPY public.beans_intake_employee (id, name, dob, is_active, is_supervisor, created_date) FROM stdin;
    public          pgadmin    false    215   F       �           0    0    beans_intake_employee_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.beans_intake_employee_id_seq', 9000004, true);
          public          pgadmin    false    214            �   l   x��4 ΀�D�����ԜN##C]]#� Dp�,��9��3��S�	�5�t�L�K).)�/&�ޘ3(?W�73'Mm�ZN��$�Ă���<<�c���� Qe3�     