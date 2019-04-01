-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le :  lun. 01 avr. 2019 à 16:52
-- Version du serveur :  5.7.19
-- Version de PHP :  7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `twitterdatabase`
--
CREATE DATABASE IF NOT EXISTS `twitterdatabase` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `twitterdatabase`;

-- --------------------------------------------------------

--
-- Structure de la table `tweet`
--

CREATE TABLE `tweet` (
  `tweetID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `created_at` varchar(30) NOT NULL,
  `text` varchar(300) NOT NULL,
  `coords` varchar(30) DEFAULT NULL,
  `city` varchar(30) NOT NULL,
  `country` varchar(30) NOT NULL,
  `bbox` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `userID` int(11) NOT NULL,
  `created_at` varchar(30) NOT NULL,
  `pseudo` varchar(30) NOT NULL,
  `country` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `tweet`
--
ALTER TABLE `tweet`
  ADD PRIMARY KEY (`tweetID`),
  ADD KEY `userID` (`userID`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userID`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `tweet`
--
ALTER TABLE `tweet`
  ADD CONSTRAINT `tweet_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `user` (`userID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
