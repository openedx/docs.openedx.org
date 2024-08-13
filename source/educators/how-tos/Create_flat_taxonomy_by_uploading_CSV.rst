Create a flat taxonomy by uploading a CSV
#########################################

Tags that can be applied to content are organized into hierarchical taxonomies. Currently, the only way to create or modify a taxonomy is by uploading a CSV or JSON file.

The simplest type of taxonomy is a flat taxonomy that doesn’t have any hierarchy. For example, if you want to tag the “difficulty” of problems as either “Easy”, “Medium”, or “Hard”, you could do that by creating a flat taxonomy. Here’s how to do that:

#. Open any spreadsheet application (Excel, Numbers, Google Sheets, etc.) and create a new blank spreadsheet. In the first row, add two columns called **id** and **value**.

   Insert image here

#. Below that, enter the new tags that you want to create in the “value” column, and give each tag an ID in the “id” column. The “id” for each tag is required, but mostly relevant when you are aligning your taxonomy with some external system that uses IDs for each tag. If you don’t have that use case, just enter the same text for the id as for the value.

   Insert image here

#. Save the spreadsheet using the default format, in case you want to edit it later.
#. Export the spreadsheet to a CSV file.

   #. In Excel, use File > Save As…, and set the “File format” to “CSV UTF-8 (comma-delimited) (.csv)” (preferred) or “Comma Separated Values (.csv)” then enter a filename and save it.
   #. In Google Sheets, use File > Download > Comma Separated Values (.csv).
   #. In Numbers, use File > Export To > CSV… and use the default options.

#. Import the taxonomy following `How-To: Import and export a taxonomy <https://openedx.atlassian.net/wiki/spaces/OEPM/pages/4154490883/How-to+Import+and+export+a+taxonomy>`_ guide.

