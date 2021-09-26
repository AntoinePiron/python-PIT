#!/bin/bash

cd .. #On vient d'abord se replacer dans le dossier racine
tar -X './sudoku_db.txt' -zcvf archive.tar.gz ./