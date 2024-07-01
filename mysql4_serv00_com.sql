-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql4.serv00.com
-- Creato il: Lug 01, 2024 alle 22:10
-- Versione del server: 8.0.35
-- Versione PHP: 8.1.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `m9800_agricontable`
--
CREATE DATABASE IF NOT EXISTS `m9800_agricontable` DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci;
USE `m9800_agricontable`;

--
-- Dump dei dati per la tabella `admin_interface_theme`
--

INSERT INTO `admin_interface_theme` (`id`, `name`, `active`, `title`, `title_visible`, `logo`, `logo_visible`, `css_header_background_color`, `title_color`, `css_header_text_color`, `css_header_link_color`, `css_header_link_hover_color`, `css_module_background_color`, `css_module_text_color`, `css_module_link_color`, `css_module_link_hover_color`, `css_module_rounded_corners`, `css_generic_link_color`, `css_generic_link_hover_color`, `css_save_button_background_color`, `css_save_button_background_hover_color`, `css_save_button_text_color`, `css_delete_button_background_color`, `css_delete_button_background_hover_color`, `css_delete_button_text_color`, `list_filter_dropdown`, `related_modal_active`, `related_modal_background_color`, `related_modal_rounded_corners`, `logo_color`, `recent_actions_visible`, `favicon`, `related_modal_background_opacity`, `env_name`, `env_visible_in_header`, `env_color`, `env_visible_in_favicon`, `related_modal_close_button_visible`, `language_chooser_active`, `language_chooser_display`, `list_filter_sticky`, `form_pagination_sticky`, `form_submit_sticky`, `css_module_background_selected_color`, `css_module_link_selected_color`, `logo_max_height`, `logo_max_width`, `foldable_apps`, `language_chooser_control`, `list_filter_highlight`, `list_filter_removal_links`, `show_fieldsets_as_tabs`, `show_inlines_as_tabs`, `css_generic_link_active_color`, `collapsible_stacked_inlines`, `collapsible_stacked_inlines_collapsed`, `collapsible_tabular_inlines`, `collapsible_tabular_inlines_collapsed`) VALUES
(1, 'Agricontable', 1, 'Amministrazione', 1, '/logo_agricontable.png', 1, '#75D367', '#EC6E05', '#44B78B', '#FFFFFF', '#C9F0DD', '#44B78B', '#FFFFFF', '#FFFFFF', '#C9F0DD', 1, '#0C3C26', '#156641', '#0C4B33', '#0C3C26', '#FFFFFF', '#BA2121', '#A41515', '#FFFFFF', 1, 1, '#000000', 1, '#FFFFFF', 1, '/agricontable-logo-micro.png', '0.3', '', 1, '#E67E22', 1, 1, 1, 'code', 1, 0, 0, '#FFFFCC', '#FFFFFF', 100, 400, 1, 'default-select', 1, 0, 0, 0, '#29B864', 0, 1, 0, 1);

--
-- Dump dei dati per la tabella `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'contabilita.admin'),
(2, 'contabilita.autore');

--
-- Dump dei dati per la tabella `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 5),
(2, 1, 6),
(3, 1, 7),
(4, 1, 8),
(5, 1, 9),
(6, 1, 10),
(7, 1, 11),
(8, 1, 12),
(9, 1, 17),
(10, 1, 18),
(11, 1, 19),
(12, 1, 20),
(13, 1, 21),
(14, 1, 22),
(15, 1, 23),
(16, 1, 24),
(17, 1, 25),
(18, 1, 26),
(19, 1, 27),
(20, 1, 28),
(21, 1, 29),
(22, 1, 30),
(23, 1, 31),
(24, 1, 32),
(25, 1, 33),
(26, 1, 34),
(27, 1, 35),
(28, 1, 36),
(29, 1, 37),
(30, 1, 38),
(31, 1, 39),
(32, 1, 40),
(33, 2, 5),
(34, 2, 6),
(35, 2, 8),
(36, 2, 9),
(37, 2, 10),
(38, 2, 12),
(39, 2, 17),
(40, 2, 18),
(41, 2, 20),
(42, 2, 24),
(43, 2, 28),
(44, 2, 29),
(45, 2, 30),
(46, 2, 31),
(47, 2, 32),
(48, 2, 33),
(49, 2, 34),
(50, 2, 35),
(51, 2, 36),
(52, 2, 37),
(53, 2, 38),
(54, 2, 39),
(55, 2, 40);

--
-- Dump dei dati per la tabella `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add Theme', 1, 'add_theme'),
(2, 'Can change Theme', 1, 'change_theme'),
(3, 'Can delete Theme', 1, 'delete_theme'),
(4, 'Can view Theme', 1, 'view_theme'),
(5, 'Can add Categoria Utente', 2, 'add_categorieutente'),
(6, 'Can change Categoria Utente', 2, 'change_categorieutente'),
(7, 'Can delete Categoria Utente', 2, 'delete_categorieutente'),
(8, 'Can view Categoria Utente', 2, 'view_categorieutente'),
(9, 'Can add Tipo Utente', 3, 'add_tipiutente'),
(10, 'Can change Tipo Utente', 3, 'change_tipiutente'),
(11, 'Can delete Tipo Utente', 3, 'delete_tipiutente'),
(12, 'Can view Tipo Utente', 3, 'view_tipiutente'),
(13, 'Can add Anagrafica Colture', 4, 'add_anagcoltura'),
(14, 'Can change Anagrafica Colture', 4, 'change_anagcoltura'),
(15, 'Can delete Anagrafica Colture', 4, 'delete_anagcoltura'),
(16, 'Can view Anagrafica Colture', 4, 'view_anagcoltura'),
(17, 'Can add Anagrafica Utente', 5, 'add_anagraficautenti'),
(18, 'Can change Anagrafica Utente', 5, 'change_anagraficautenti'),
(19, 'Can delete Anagrafica Utente', 5, 'delete_anagraficautenti'),
(20, 'Can view Anagrafica Utente', 5, 'view_anagraficautenti'),
(21, 'Can add Conto', 6, 'add_contocoge'),
(22, 'Can change Conto', 6, 'change_contocoge'),
(23, 'Can delete Conto', 6, 'delete_contocoge'),
(24, 'Can view Conto', 6, 'view_contocoge'),
(25, 'Can add Tipo di Documento di contabilità', 7, 'add_tipidoccoge'),
(26, 'Can change Tipo di Documento di contabilità', 7, 'change_tipidoccoge'),
(27, 'Can delete Tipo di Documento di contabilità', 7, 'delete_tipidoccoge'),
(28, 'Can view Tipo di Documento di contabilità', 7, 'view_tipidoccoge'),
(29, 'Can add Prima Nota Contabile', 8, 'add_pncgen'),
(30, 'Can change Prima Nota Contabile', 8, 'change_pncgen'),
(31, 'Can delete Prima Nota Contabile', 8, 'delete_pncgen'),
(32, 'Can view Prima Nota Contabile', 8, 'view_pncgen'),
(33, 'Can add Riga', 9, 'add_pncrighe'),
(34, 'Can change Riga', 9, 'change_pncrighe'),
(35, 'Can delete Riga', 9, 'delete_pncrighe'),
(36, 'Can view Riga', 9, 'view_pncrighe'),
(37, 'Can add pnc tes', 10, 'add_pnctes'),
(38, 'Can change pnc tes', 10, 'change_pnctes'),
(39, 'Can delete pnc tes', 10, 'delete_pnctes'),
(40, 'Can view pnc tes', 10, 'view_pnctes'),
(41, 'Can add log entry', 11, 'add_logentry'),
(42, 'Can change log entry', 11, 'change_logentry'),
(43, 'Can delete log entry', 11, 'delete_logentry'),
(44, 'Can view log entry', 11, 'view_logentry'),
(45, 'Can add permission', 12, 'add_permission'),
(46, 'Can change permission', 12, 'change_permission'),
(47, 'Can delete permission', 12, 'delete_permission'),
(48, 'Can view permission', 12, 'view_permission'),
(49, 'Can add group', 13, 'add_group'),
(50, 'Can change group', 13, 'change_group'),
(51, 'Can delete group', 13, 'delete_group'),
(52, 'Can view group', 13, 'view_group'),
(53, 'Can add user', 14, 'add_user'),
(54, 'Can change user', 14, 'change_user'),
(55, 'Can delete user', 14, 'delete_user'),
(56, 'Can view user', 14, 'view_user'),
(57, 'Can add content type', 15, 'add_contenttype'),
(58, 'Can change content type', 15, 'change_contenttype'),
(59, 'Can delete content type', 15, 'delete_contenttype'),
(60, 'Can view content type', 15, 'view_contenttype'),
(61, 'Can add session', 16, 'add_session'),
(62, 'Can change session', 16, 'change_session'),
(63, 'Can delete session', 16, 'delete_session'),
(64, 'Can view session', 16, 'view_session');

--
-- Dump dei dati per la tabella `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$zQbCxd7jPCtDGSdIGXGISL$Lsa/ouZ0BvVlJF/fp6Hyg9NC0A6GphC5hRUSPwxk9vw=', '2024-06-30 18:20:37.456316', 1, 'bleish', '', '', 'bleish@gmail.com', 1, 1, '2024-06-29 18:02:10.794467'),
(2, 'pbkdf2_sha256$720000$YPnAwzyWvomWm1j5RC3Bax$BM0ULWyrsopJtaPjRIQdMLEj7wDdyymAd0qXX5KCDPs=', NULL, 0, 'utente.autore', 'Autore', 'contabilità', '', 0, 1, '2024-07-01 16:17:04.000000'),
(3, 'pbkdf2_sha256$720000$WVq84B4GEFQ17VS50cemaN$KV/S3iQeCUYYSJEKzv3KWP1G2y/QrsVLllsDTphnlUc=', NULL, 0, 'utente.lettoreq', '', '', '', 0, 1, '2024-07-01 16:17:25.738895'),
(4, 'pbkdf2_sha256$720000$zoIuJ3VZ40lZZCW7g0UT2b$e4NGXS/cf6AbdgQ8PSNUpC2d4kvmVzh50dOdZ8F9SXk=', NULL, 0, 'ADMINcontable', 'Amminsitratore', 'Di contabilità', '', 0, 1, '2024-07-01 16:23:43.000000');

--
-- Dump dei dati per la tabella `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 2),
(2, 4, 1);

--
-- Dump dei dati per la tabella `contable_contocoge`
--

INSERT INTO `contable_contocoge` (`id`, `nome`, `descrizione`, `lft`, `rght`, `tree_id`, `level`, `parent_id`) VALUES
(1, '01', 'costo generale', 1, 8, 1, 0, NULL),
(2, '51', 'ricavo generale', 1, 4, 2, 0, NULL),
(3, '01', 'costo personale', 2, 7, 1, 1, 1),
(4, '01', 'personale avventizio', 3, 4, 1, 2, 3),
(5, '01', 'ricavo vendite', 2, 3, 2, 1, 2),
(6, '02', 'Personale OTI', 5, 6, 1, 2, 3);

--
-- Dump dei dati per la tabella `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-06-29 18:11:58.599416', '1', '01 - costo generale', 1, '[{\"added\": {}}]', 6, 1),
(2, '2024-06-29 18:16:03.748090', '1', '01 - costo generale', 2, '[]', 6, 1),
(3, '2024-06-29 18:16:17.059717', '2', '51 - ricavo generale', 1, '[{\"added\": {}}]', 6, 1),
(4, '2024-06-29 18:16:28.727427', '3', '01.01 - costo personale', 1, '[{\"added\": {}}]', 6, 1),
(5, '2024-06-29 18:16:48.794663', '4', '01.01.01 - personale avventizio', 1, '[{\"added\": {}}]', 6, 1),
(6, '2024-06-29 18:17:02.327359', '5', '51.01 - ricavo vendite', 1, '[{\"added\": {}}]', 6, 1),
(7, '2024-06-29 18:32:49.979981', '1', 'Agricontable', 2, '[{\"changed\": {\"fields\": [\"Background color\"]}}]', 1, 1),
(8, '2024-06-29 18:33:21.240537', '1', 'Agricontable', 2, '[{\"changed\": {\"fields\": [\"Color\"]}}]', 1, 1),
(9, '2024-06-29 18:34:38.071645', '1', 'Agricontable', 2, '[{\"changed\": {\"fields\": [\"Color\"]}}]', 1, 1),
(10, '2024-06-29 18:35:07.970835', '1', 'Agricontable', 2, '[{\"changed\": {\"fields\": [\"Color\"]}}]', 1, 1),
(11, '2024-06-30 00:13:06.486604', '4', '01.01.01 - personale avventizio', 2, '[]', 6, 1),
(12, '2024-06-30 18:22:38.310535', '6', '01.01.02 - Personale OTI', 1, '[{\"added\": {}}]', 6, 1),
(13, '2024-06-30 18:29:34.746189', '1', '01 - costo generale', 2, '[]', 6, 1),
(14, '2024-07-01 16:17:05.598729', '2', 'utente.autore', 1, '[{\"added\": {}}]', 14, 1),
(15, '2024-07-01 16:17:26.386049', '3', 'utente.lettoreq', 1, '[{\"added\": {}}]', 14, 1),
(16, '2024-07-01 16:18:39.088724', '2', 'utente.autore', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 14, 1),
(17, '2024-07-01 16:21:09.903265', '1', 'contabilita.admin', 1, '[{\"added\": {}}]', 13, 1),
(18, '2024-07-01 16:22:41.175809', '2', 'contabilita.autore', 1, '[{\"added\": {}}]', 13, 1),
(19, '2024-07-01 16:23:26.462331', '2', 'utente.autore', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 14, 1),
(20, '2024-07-01 16:23:43.672238', '4', 'ADMINcontable', 1, '[{\"added\": {}}]', 14, 1),
(21, '2024-07-01 16:24:17.231590', '4', 'ADMINcontable', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Groups\"]}}]', 14, 1);

--
-- Dump dei dati per la tabella `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(11, 'admin', 'logentry'),
(1, 'admin_interface', 'theme'),
(4, 'anag_utenti', 'anagcoltura'),
(5, 'anag_utenti', 'anagraficautenti'),
(2, 'anag_utenti', 'categorieutente'),
(3, 'anag_utenti', 'tipiutente'),
(13, 'auth', 'group'),
(12, 'auth', 'permission'),
(14, 'auth', 'user'),
(6, 'contable', 'contocoge'),
(8, 'contable', 'pncgen'),
(9, 'contable', 'pncrighe'),
(10, 'contable', 'pnctes'),
(7, 'contable', 'tipidoccoge'),
(15, 'contenttypes', 'contenttype'),
(16, 'sessions', 'session');

--
-- Dump dei dati per la tabella `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-29 17:59:56.100375'),
(2, 'auth', '0001_initial', '2024-06-29 17:59:56.377069'),
(3, 'admin', '0001_initial', '2024-06-29 17:59:56.448604'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-06-29 17:59:56.474400'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-29 17:59:56.486024'),
(6, 'admin_interface', '0001_initial', '2024-06-29 17:59:56.512104'),
(7, 'admin_interface', '0002_add_related_modal', '2024-06-29 17:59:56.642449'),
(8, 'admin_interface', '0003_add_logo_color', '2024-06-29 17:59:56.735269'),
(9, 'admin_interface', '0004_rename_title_color', '2024-06-29 17:59:56.764080'),
(10, 'admin_interface', '0005_add_recent_actions_visible', '2024-06-29 17:59:56.794973'),
(11, 'admin_interface', '0006_bytes_to_str', '2024-06-29 17:59:56.963444'),
(12, 'admin_interface', '0007_add_favicon', '2024-06-29 17:59:57.003839'),
(13, 'admin_interface', '0008_change_related_modal_background_opacity_type', '2024-06-29 17:59:57.071503'),
(14, 'admin_interface', '0009_add_enviroment', '2024-06-29 17:59:57.157067'),
(15, 'admin_interface', '0010_add_localization', '2024-06-29 17:59:57.208034'),
(16, 'admin_interface', '0011_add_environment_options', '2024-06-29 17:59:57.371242'),
(17, 'admin_interface', '0012_update_verbose_names', '2024-06-29 17:59:57.383420'),
(18, 'admin_interface', '0013_add_related_modal_close_button', '2024-06-29 17:59:57.417607'),
(19, 'admin_interface', '0014_name_unique', '2024-06-29 17:59:57.441370'),
(20, 'admin_interface', '0015_add_language_chooser_active', '2024-06-29 17:59:57.470884'),
(21, 'admin_interface', '0016_add_language_chooser_display', '2024-06-29 17:59:57.510015'),
(22, 'admin_interface', '0017_change_list_filter_dropdown', '2024-06-29 17:59:57.535276'),
(23, 'admin_interface', '0018_theme_list_filter_sticky', '2024-06-29 17:59:57.569672'),
(24, 'admin_interface', '0019_add_form_sticky', '2024-06-29 17:59:57.654948'),
(25, 'admin_interface', '0020_module_selected_colors', '2024-06-29 17:59:57.793183'),
(26, 'admin_interface', '0021_file_extension_validator', '2024-06-29 17:59:57.818773'),
(27, 'admin_interface', '0022_add_logo_max_width_and_height', '2024-06-29 17:59:57.912302'),
(28, 'admin_interface', '0023_theme_foldable_apps', '2024-06-29 17:59:57.959033'),
(29, 'admin_interface', '0024_remove_theme_css', '2024-06-29 17:59:57.985747'),
(30, 'admin_interface', '0025_theme_language_chooser_control', '2024-06-29 17:59:58.028757'),
(31, 'admin_interface', '0026_theme_list_filter_highlight', '2024-06-29 17:59:58.071072'),
(32, 'admin_interface', '0027_theme_list_filter_removal_links', '2024-06-29 17:59:58.128458'),
(33, 'admin_interface', '0028_theme_show_fieldsets_as_tabs_and_more', '2024-06-29 17:59:58.247678'),
(34, 'admin_interface', '0029_theme_css_generic_link_active_color', '2024-06-29 17:59:58.305451'),
(35, 'admin_interface', '0030_theme_collapsible_stacked_inlines_and_more', '2024-06-29 17:59:58.472169'),
(36, 'contenttypes', '0002_remove_content_type_name', '2024-06-29 17:59:58.566804'),
(37, 'auth', '0002_alter_permission_name_max_length', '2024-06-29 17:59:58.624469'),
(38, 'auth', '0003_alter_user_email_max_length', '2024-06-29 17:59:58.734385'),
(39, 'auth', '0004_alter_user_username_opts', '2024-06-29 17:59:58.796323'),
(40, 'auth', '0005_alter_user_last_login_null', '2024-06-29 17:59:58.868026'),
(41, 'auth', '0006_require_contenttypes_0002', '2024-06-29 17:59:58.870474'),
(42, 'auth', '0007_alter_validators_add_error_messages', '2024-06-29 17:59:58.881850'),
(43, 'auth', '0008_alter_user_username_max_length', '2024-06-29 17:59:58.921522'),
(44, 'auth', '0009_alter_user_last_name_max_length', '2024-06-29 17:59:58.967933'),
(45, 'auth', '0010_alter_group_name_max_length', '2024-06-29 17:59:59.020547'),
(46, 'auth', '0011_update_proxy_permissions', '2024-06-29 17:59:59.077410'),
(47, 'auth', '0012_alter_user_first_name_max_length', '2024-06-29 17:59:59.127582'),
(48, 'sessions', '0001_initial', '2024-06-29 17:59:59.151364'),
(49, 'anag_utenti', '0001_initial', '2024-06-29 18:11:01.264431'),
(50, 'contable', '0001_initial', '2024-06-29 18:11:01.838363');

--
-- Dump dei dati per la tabella `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('510wzddj9bhxlv1l624pvvkm1p9l6e29', '.eJxVjMEOgjAQRP-lZ9NAKaXr0Tvf0Ox2F4uaNqFwMv67kHDQ22Tem3mrgNuawlZlCTOrq2rV5bcjjE_JB-AH5nvRseR1mUkfij5p1WNhed1O9-8gYU37Whx05JgbsTa23rDnXmiKYCYiGdwRoDcdsPetkwa7fjcQBkdkG0D1-QL-HThO:1sNhwi:RTAc7rOjxk7mlEqnui3mrdWTK7_NYdixNcGZFaI3NIU', '2024-07-13 23:57:32.249359'),
('g5pumqruwaayb75wz6nbxv4hzpci9dzz', '.eJxVjMEOgjAQRP-lZ9NAKaXr0Tvf0Ox2F4uaNqFwMv67kHDQ22Tem3mrgNuawlZlCTOrq2rV5bcjjE_JB-AH5nvRseR1mUkfij5p1WNhed1O9-8gYU37Whx05JgbsTa23rDnXmiKYCYiGdwRoDcdsPetkwa7fjcQBkdkG0D1-QL-HThO:1sNyH0:JnNe5DK8okP6cc9XOPe57yeCH7BQTNh5RAqqWgzQyzc', '2024-07-14 17:23:34.866304'),
('r85qdatkcbmiry1je5ub8fr4nh06vsfz', '.eJxVjMEOgjAQRP-lZ9NAKaXr0Tvf0Ox2F4uaNqFwMv67kHDQ22Tem3mrgNuawlZlCTOrq2rV5bcjjE_JB-AH5nvRseR1mUkfij5p1WNhed1O9-8gYU37Whx05JgbsTa23rDnXmiKYCYiGdwRoDcdsPetkwa7fjcQBkdkG0D1-QL-HThO:1sNezd:1PIBNQO2872dmf-zZ4CHE8xSdeFTd58UX2ou4sDsN_A', '2024-07-13 20:48:21.831232'),
('uyrhiefxx0wok5ywmjx4ll9egq31gifg', '.eJxVjMEOgjAQRP-lZ9NAKaXr0Tvf0Ox2F4uaNqFwMv67kHDQ22Tem3mrgNuawlZlCTOrq2rV5bcjjE_JB-AH5nvRseR1mUkfij5p1WNhed1O9-8gYU37Whx05JgbsTa23rDnXmiKYCYiGdwRoDcdsPetkwa7fjcQBkdkG0D1-QL-HThO:1sNzAD:BeSRFY-ydFvE47ljFledWxWMzy20Hid9B554JOGBF-g', '2024-07-14 18:20:37.458421');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
