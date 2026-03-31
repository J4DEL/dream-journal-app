This is Version 1 of my personal dream journal app. I built this in Python to learn GUI development, File I/O, and AES encryption. 
I am currently rebuilding Version 2 from scratch in Java!

Dream Journal - V1 Feature Blueprint
Project Overview

Goal: A secure, local desktop application for logging and analyzing dream entries.

Target V2 Stack: Java, JavaFX, SceneBuilder. (V1 was built in Python/Tkinter).

Core Data Pipeline & Storage

Input: Users type a dream into a multi-line text area and check a boolean box if it was a "Lucid Dream".

Formatting: If lucid, the tag [#LUCID] is appended to the text string.

Storage: Entries are saved locally to a dream.txt file. Multiple entries are separated by a specific delimiter (\n---\n).

Security Architecture (Critical)

Authentication: The app prompts the user for a hardcoded PIN (e.g., "2026") before granting read access to the vault.

Encryption: All text is encrypted using AES (symmetric encryption) before being written to the .txt file.

Key Management: A master AES key is generated via a separate, isolated script and saved locally as a hidden .secret.key file. The main application only has read-access to this key to encrypt/decrypt.

Data Dashboard & Analytics

Decryption Pipeline: The app reads the .txt file, splits the encrypted chunks by the delimiter, and decrypts them back into readable text.

Data Structuring: The app parses the decrypted text to check for the [#LUCID] tag and builds a structured dataset (e.g., a list of dictionaries/objects with "Dream" text and "Lucid" boolean).

Analytics: It calculates the total number of dreams logged and the "Lucidity Success Rate (%)".

UI Display: These stats are displayed at the top of a secondary "Past Dreams Vault" window, followed by the decrypted text of all past entries.