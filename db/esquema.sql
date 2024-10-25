-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3307
-- Tiempo de generación: 05-10-2024 a las 00:17:18
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `libreria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor`
--

CREATE TABLE `autor` (
  `id_aut` int(11) NOT NULL,
  `nom_aut` varchar(100) NOT NULL,
  `apePat_aut` varchar(100) NOT NULL,
  `apeMat_aut` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autor_libro`
--

CREATE TABLE `autor_libro` (
  `id_aut` int(11) NOT NULL,
  `isbn_lib` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editorial`
--

CREATE TABLE `editorial` (
  `id_edi` int(11) NOT NULL,
  `nom_edi` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id_gen` int(11) NOT NULL,
  `nom_gen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lector`
--

CREATE TABLE `lector` (
  `dni_lec` char(8) NOT NULL,
  `nom_lec` varchar(100) NOT NULL,
  `apePat_lec` varchar(100) NOT NULL,
  `apeMat_lec` varchar(100) NOT NULL,
  `email_lec` varchar(255) NOT NULL,
  `pws_lec` varchar(50) NOT NULL,
  `fecha_nac` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `lector`
--

INSERT INTO `lector` (`dni_lec`, `nom_lec`, `apePat_lec`, `apeMat_lec`, `email_lec`, `pws_lec`, `fecha_nac`) VALUES
('78695446', 'Claudio', 'Asenjo', 'Vasquez', 'darthkirby@gmail.com', 'Undeath', '2002-08-08');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro`
--

CREATE TABLE `libro` (
  `isbn_lib` varchar(13) NOT NULL,
  `titulo_lib` varchar(100) NOT NULL,
  `añoPub_lib` int(11) NOT NULL,
  `estado_lib` bit(1) NOT NULL,
  `clasificacion` varchar(10) NOT NULL,
  `id_edi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libro_genero`
--

CREATE TABLE `libro_genero` (
  `id_gen` int(11) NOT NULL,
  `isbn_lib` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo`
--

CREATE TABLE `prestamo` (
  `id_pre` int(11) NOT NULL,
  `fec_pre` date NOT NULL,
  `fecVenc_pre` date NOT NULL,
  `estado_pre` bit(1) NOT NULL,
  `dni_lec` char(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamo_libro`
--

CREATE TABLE `prestamo_libro` (
  `id_pre` int(11) NOT NULL,
  `isbn_lib` varchar(13) NOT NULL,
  `precio_pre` decimal(9,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `id_ven` int(11) NOT NULL,
  `fec_ven` date NOT NULL,
  `estado_ven` bit(1) NOT NULL,
  `dni_lec` char(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta_libro`
--

CREATE TABLE `venta_libro` (
  `id_ven` int(11) NOT NULL,
  `isbn_lib` varchar(13) NOT NULL,
  `precio_ven` decimal(9,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id_aut`);

--
-- Indices de la tabla `autor_libro`
--
ALTER TABLE `autor_libro`
  ADD PRIMARY KEY (`id_aut`,`isbn_lib`),
  ADD KEY `FKautor_libr68279` (`isbn_lib`);

--
-- Indices de la tabla `editorial`
--
ALTER TABLE `editorial`
  ADD PRIMARY KEY (`id_edi`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id_gen`);

--
-- Indices de la tabla `lector`
--
ALTER TABLE `lector`
  ADD PRIMARY KEY (`dni_lec`);

--
-- Indices de la tabla `libro`
--
ALTER TABLE `libro`
  ADD PRIMARY KEY (`isbn_lib`),
  ADD KEY `FKlibro384308` (`id_edi`);

--
-- Indices de la tabla `libro_genero`
--
ALTER TABLE `libro_genero`
  ADD PRIMARY KEY (`id_gen`,`isbn_lib`),
  ADD KEY `FKlibro_gene975528` (`isbn_lib`);

--
-- Indices de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD PRIMARY KEY (`id_pre`),
  ADD KEY `FKprestamo426987` (`dni_lec`);

--
-- Indices de la tabla `prestamo_libro`
--
ALTER TABLE `prestamo_libro`
  ADD PRIMARY KEY (`id_pre`,`isbn_lib`),
  ADD KEY `FKprestamo_l951090` (`isbn_lib`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`id_ven`),
  ADD KEY `FKventa217506` (`dni_lec`);

--
-- Indices de la tabla `venta_libro`
--
ALTER TABLE `venta_libro`
  ADD PRIMARY KEY (`id_ven`,`isbn_lib`),
  ADD KEY `FKventa_libr843845` (`isbn_lib`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autor`
--
ALTER TABLE `autor`
  MODIFY `id_aut` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `editorial`
--
ALTER TABLE `editorial`
  MODIFY `id_edi` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id_gen` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `prestamo`
--
ALTER TABLE `prestamo`
  MODIFY `id_pre` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `venta`
--
ALTER TABLE `venta`
  MODIFY `id_ven` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `autor_libro`
--
ALTER TABLE `autor_libro`
  ADD CONSTRAINT `FKautor_libr68279` FOREIGN KEY (`isbn_lib`) REFERENCES `libro` (`isbn_lib`),
  ADD CONSTRAINT `FKautor_libr900102` FOREIGN KEY (`id_aut`) REFERENCES `autor` (`id_aut`);

--
-- Filtros para la tabla `libro`
--
ALTER TABLE `libro`
  ADD CONSTRAINT `FKlibro384308` FOREIGN KEY (`id_edi`) REFERENCES `editorial` (`id_edi`);

--
-- Filtros para la tabla `libro_genero`
--
ALTER TABLE `libro_genero`
  ADD CONSTRAINT `FKlibro_gene459369` FOREIGN KEY (`id_gen`) REFERENCES `genero` (`id_gen`),
  ADD CONSTRAINT `FKlibro_gene975528` FOREIGN KEY (`isbn_lib`) REFERENCES `libro` (`isbn_lib`);

--
-- Filtros para la tabla `prestamo`
--
ALTER TABLE `prestamo`
  ADD CONSTRAINT `FKprestamo426987` FOREIGN KEY (`dni_lec`) REFERENCES `lector` (`dni_lec`);

--
-- Filtros para la tabla `prestamo_libro`
--
ALTER TABLE `prestamo_libro`
  ADD CONSTRAINT `FKprestamo_l169722` FOREIGN KEY (`id_pre`) REFERENCES `prestamo` (`id_pre`),
  ADD CONSTRAINT `FKprestamo_l951090` FOREIGN KEY (`isbn_lib`) REFERENCES `libro` (`isbn_lib`);

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `FKventa217506` FOREIGN KEY (`dni_lec`) REFERENCES `lector` (`dni_lec`);

--
-- Filtros para la tabla `venta_libro`
--
ALTER TABLE `venta_libro`
  ADD CONSTRAINT `FKventa_libr724635` FOREIGN KEY (`id_ven`) REFERENCES `venta` (`id_ven`),
  ADD CONSTRAINT `FKventa_libr843845` FOREIGN KEY (`isbn_lib`) REFERENCES `libro` (`isbn_lib`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
