.. _layers.upload:

Uploading a layer
=================

Now that we have taken a tour of GeoNode and viewed existing layers, the next step is to upload our own.

In your data pack is a directory called :file:`data`. Inside that directory is a shapefile called :file:`airports.shp`. This is a data set containing world airports and various other details associated with them. This will be the first layer that we upload to GeoNode.

#. Navigate to the main GeoNode homepage. For this workshop, this page is located at ``http://localhost:8080/geonode``.

   .. figure:: img/geonodehome.png
      :width: 50%
      :align: center

      *GeoNode homepage*

#. Click the :guilabel:`Layers` link on the top toolbar. This will bring up the Layers menu.

   .. figure:: img/toolbar.png
      :width: 50%
      :align: center

      *Main toolbar for GeoNode*

   .. figure:: img/explorelayers.png
      :width: 50%
      :align: center

      *Layers submenu*

#. Click :guilabel:`Upload Layers` in the Layers toolbar.

   .. figure:: img/layerstoolbar.png
      :width: 50%
      :align: center

      *Layers toolbar*

   .. figure:: img/uploadform.png
      :width: 50%
      :align: center

      *Upload Layers form*

#. Fill out the form.

  * In the :guilabel:`Title` field, enter ``airports``.

  * Next to the :guilabel:`Data` field, click the :guilabel:`Browse...` button. This will bring up a local file dialog. Navigate to your data folder and select the :file:`airports.shp` shapefile.

.. todo:: Continue on...