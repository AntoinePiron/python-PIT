#!/bin/bash

cd .. #On vient d'abord se replacer dans le dossier racine
tar --exclude='./sudoku_db.txt' -zcvf archive.tar.gz ./