# PyPDF2_Fields

## Français

La bibliothèque PyPDF2_Fields est un complément à PyPDF2. Elle aide à
l’utilisation des champs d’un fichier PDF en facilitant les tâches suivantes.

* Lire la valeur contenue dans les champs
* Modifier la valeur contenue dans les champs
* Identifier le type d’un champ
* Assurer la visibilité du contenu des champs
* Déterminer si les champs d’un fichier PDF généré par une application seront
modifiables

À cette fin, PyPDF2_Fields fournit les fonctions ci-dessous.

* **`get_field_type`**

Identifie le type d’un champ d’un fichier PDF. La valeur renvoyée est un membre
de l’énumeration `PdfFieldType`, aussi incluse dans cette bibliothèque.

* **`make_writer_from_reader`**

Crée un objet `PdfFileWriter` dont le contenu est identique à celui de l’objet
`PdfFileReader` donné. Selon le choix de l’appelant, cet écriveur produira un
fichier modifiable ou non.

* **`pdf_field_name_val_dict`**

Constitue un dictionnaire associant le nom des champs à leur valeur.

* **`set_need_appearances`**

Assure qu’un `PdfFileWriter` produira un fichier dont le contenu des champs
sera visible.

* **`update_page_fields`**

Définit la valeur des champs de texte, des boîtes à cocher et des groupes de
boutons radio. Cette fonction utilise des instances de la classe
`RadioBtnGroup`, aussi incluse dans cette bibliothèque.

## English

Library PyPDF2_Fields is a complement to PyPDF2. It helps using a PDF file’s
fields by facilitating the following tasks.

* Reading the value contained in the fields
* Setting the value contained in the fields
* Identifying a field’s type
* Ensuring the visibility of the fields’ content
* Determining whether the fields of a PDF file generated by an application
will be editable

For this purpose, PyPDF2 provides the functions below.

* **`get_field_type`**

Identifies the type of a field from a PDF file. The returned value is a member
of enumeration `PdfFieldType`, which is also included in this library.

* **`make_writer_from_reader`**

Creates a `PdfFileWriter` object whose content is identical to that of the
given `PdfFileReader` object. Depending on the caller’s choice, the file
produced by that writer will be editable or not.

* **`pdf_field_name_val_dict`**

Creates a dictionary that maps the fields’ name to their value.

* **`set_need_appearances`**

Ensures that a `PdfFileWriter` will produce a file with fields whose content
will be visible.

* **`update_page_fields`**

Sets the value of text fields, checkboxes and radio button groups. This
function uses instances of class `RadioBtnGroup`, which is also included in
this library.
