# landsat-MTL-C2toC1

Landsat data provided by the USGS are distributed as a single file in an archived and zipped ".TAR" format. These files must be extracted and uncompressed before you can use them.

In ENVI 5, open the metadata file (MTL.txt)  through **File> Open as> Landsat> GeoTIFF with Metadata** to import Landsat Collection 1 Level 1 image with all bands in the correct order.

At the end of 2020, USGS released [Landsat Collection 2](https://www.usgs.gov/center-news/december-7-2020-new-landsat-update-special-issue-landsat-collection-2-now-available?qt-news_science_products=4#qt-news_science_products).

> **Collection 2 Improvements include:**
> - Substantial improvement in the absolute geolocation accuracy of the global ground reference dataset which improves interoperability with Europe's Copernicus Sentinel-2 mission;
> - Updated global digital elevation modeling sources;
> - Calibration and validation updates;
> - Accessible from a commercial cloud-based environment.
> ref: [https://www.usgs.gov/core-science-systems/nli/landsat/landsat-update-special-issue-december-2020](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-update-special-issue-december-2020)

There are [enhancements and changes between Collection 1 and Collection 2 Level-1 metadata](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-metadata), the current highest version of ENVI (ENVI 5.6) has not yet supported the reading of Landsat Collection 2 MTL files.


Modifying the MTL file in batches manually is time-consuming, here is a script to do it:
<br /> 
**Put the MTL files of Collection 2 format into the ****inputs folder**** in the same directory. After the script runs, the converted MTL file of Collection 1 format will be generated in the ****outputs folder**** in the same directory.**

In this repository, you can find:
- **A source code based on python 3.6;**
- **An executable file for more convenient use bundled by package **[**PyInstaller**](https://www.pyinstaller.org/)**;**
- **Sample files in inputs folder and outputs folders.**

**Note:** 
There is no **GROUP = PRODUCT_PARAMETERS** in the sample MTL files, so **"Can't find PRODUCT_PARAMETERS"** will be printed. This error has no effect on the generation result.


