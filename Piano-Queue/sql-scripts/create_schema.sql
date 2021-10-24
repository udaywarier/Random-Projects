/* The database that I'm storing all the information in for this project. */
USE random_projects;

/* Tear down the table if it already exists. */
DROP TABLE IF EXISTS PianoQueue;

/* Recreate the schema from scratch. */
CREATE TABLE PianoQueue (
    SongID int NOT NULL AUTO_INCREMENT,
    SongName varchar(255) NOT NULL,
    SongArtist varchar(255) NOT NULL,
    PRIMARY KEY(SongID)
);