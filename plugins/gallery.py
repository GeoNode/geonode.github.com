# -*- coding: utf-8 -*-


class GalleryItem(object):

    def __init__(self, title, subtitle=None, description=None, screenshot=None, screenshot_width=325,
                 screenshot_height=178, region=None, url=None):

        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.screenshot = screenshot
        self.screenshot_width= screenshot_width
        self.screenshot_height= screenshot_height
        self.region = region
        self.url = url


bolivia = GalleryItem('Bolivia GeoNode',
                      description='Bolivia is using GeoNode to develop a \
                                   Geographical Data Infrastructure for the National Information System for Risk \
                                   Reduction, composed by science and specialised sectors in the areas of; Risk \
                                   management, Geological Survey, National Statistics, MilitaryGeographical Institute,\
                                   Heath, Land, Water and education sectors. Each sector will have an instance of \
                                   GeoNode, and all the be federated in one system  orchestrated by the Civil Defence\
                                   Office. A few examples of Bolivia\'s instances are below: <ul class="unstyled"> \
                                   <li><a href= "http://geosinager.defensacivil.gob.bo/">http://geosinager.defensacivil.gob.bo/</a></li> \
                                   <li><a href= "http://georiesgos.sergeotecmin.gob.bo/">http://georiesgos.sergeotecmin.gob.bo/</a></li> \
                                   <li><a href= "http://geonode.igmbolivia.gob.bo/">http://geonode.igmbolivia.gob.bo/</a></li> \
                                   <li><a href= "http://mapas.senamhi.gob.bo/">http://mapas.senamhi.gob.bo/</a></li>\
                                   <li><a href= "http://geosinager.defensacivil.gob.bo/">http://geosinager.defensacivil.gob.bo/</a></li>\
                                   </ul>',
                      screenshot="../static/img/bolivia.png",
                      screenshot_width=325,
                      screenshot_height=178,
                      region="americas",
                      url="http://geosinager.defensacivil.gob.bo"
                      )

cba = GalleryItem('Caribbean Risk Atlas',
                      subtitle="UMI DRRC",
                      description='The University of the West Indies (UWI) Disaster Risk Reduction Centre (DRRC) and \
                                   the World Bank collaborated on the "Caribbean Risk Atlas" project with the main \
                                   goal of making spatial data on risk for hurricanes, earthquakes and floods in the \
                                   Caribbean available on-line. Mona GeoInformatics Institute (MGI) built the "Cariska"\
                                   web map application for this project on the GeoNode platform.',

                      screenshot="../static/img/cariska.png",
                      screenshot_width=325,
                      screenshot_height=178,
                      region="americas",
                      url="http://cariska.mona.uwi.edu"
                      )

cigno = GalleryItem('CIGNo',
                    "National Council of Research ISMAR",
                    description="The CIGNO (Collaborative Interoperable Geographic NOde) geoportal system is proposed \
                                to implement a system for heterogeneous multimedia data and metadata management \
                                (scientific and geographical, textual documents, tables, etc...). CIGNO can help users \
                                (stakeholders, administrators, scientists) to consult and exploit the scientific \
                                information provided by the ISMAR researchers.",
                    region="americas",
                    screenshot="../static/img/cigno.png",
                    url='http://cigno.ve.ismar.cnr.it'
                    )

haiti = GalleryItem('HaitiData.org',
                    "The World Bank",
                    description="HaitiData is designed toto facilitate open access to Haiti-related \
                                 geo-spatial information, data and knowledge sources, encouraging \
                                 others to share and use them for the development of Haiti. \
                                 For a list of all the organizations and people involved in data \
                                 collection for the site, see the <a href= \"http://haitidata.org/partners/\">partners page.</a>",
                    region="americas",
                    screenshot="../static/img/haiti.png",
                    screenshot_width=325,
                    screenshot_height=222,
                    url="http://haitidata.org"
                    )

mapstory = GalleryItem("MapStory",
                       "MapStory Foundation",
                       description="MapStory, as a compliment to Wikipedia, is a new dimension to the global data    \
                                   commons that empowers a global user community to organize all knowledge about the \
                                   world spatially and temporally. Just as Wikipedia uses a MediaWiki, MapStory uses \
                                   a GeoNode.  Perhaps more important, MapStory is an infrastructure for enabling \
                                   \"MapStorytelling\" as a means of communicating important issues to a global \
                                   audience.  In order to accomplish this, MapStory has sponsored temporal, social and \
                                   narrative extensions to GeoNode.  The goal is to enable any student, teacher or \
                                   practitioner on Earth to tap the power of this new mode of conveying one\'s stories,\
                                   arrayed across geography and as they unfold over time. MapStory will become the \
                                   convening point where MapStorytellers of all kinds come to publish their\
                                   expressions, and to critique each others\' MapStories, leading to a consistently \
                                   accumulating and improving global body of knowledge about global dynamics, \
                                   worldwide, over the course of history.",
                       region="worldwide",
                       screenshot="../static/img/mapstory.png",
                       screenshot_height=187,
                       url="http://www.mapstory.org"
                       )

masdap = GalleryItem("MASDAP",
                     "Created by GFDRR and the World Bank",
                     description="The Government of Malawi, in partnership with the GFDRR labs of the World Bank is \
                                  using GeoNode with data coming from the various ministries to build resilience to \
                                  disasters in a changing climate.",
                     region="worldwide",
                     screenshot="../static/img/masdap.png",
                     screenshot_height=189,
                     url="http://23.22.63.123")

montagneAperte = GalleryItem("montagneAperte",
                             "GfosServices",
                             description="The Mountain community of Monti Martani, Seranoand Subasio is using Geonode \
                                         to share  spatial data such like hiking trails and other distrincitve outdoor \
                                         feautures.",
                             region="worldwide",
                             screenshot="../static/img/montagne.png",
                             screenshot_height=189,
                             url="http://www.montagneaperte.it"
                             )

mozadapt = GalleryItem("Moz Adapt",
                       "INGC and The World Bank",
                       description="The purpose of moz-adapt.org is to provide tools and data in order to \
                                   better understand and prepare for Climate Change in the country of Mozambique \
                                   with an enfasis on reducing disasters caused by natural hazards. \
                                   The site has been developed by and for INGC, with support from The World Bank, \
                                   The Global Facility for Disaster Reduction and Recovery (GFDRR).",
                       region="africa",
                       screenshot="../static/img/moz.png",
                       screenshot_height=243,
                       url="http://moz-adapt.org"
                       )

paris = GalleryItem("PaRIS",
                    "SOPAC",
                    description="Pacific Risk Information Systems (PaRIS) is one of the largest     \
                                 collections of geospatial information for the Pacific island region.\
                                 PaRIS was assembled to provide detailed probabilistic risk information \
                                 for 15 Pacific island countries for a range of decision makers \
                                 including disaster risk management agencies. The perils covered are \
                                 tropical cyclones (wind, storm surge and rain) and earthquakes (ground \
                                 shaking, tsunami). The countries covered are Cook Islands, Fiji, \
                                 Kiribati, Marshall Islands, Federated States of Micronesia, Nauru,\
                                 Niue, Palau, Papua New Guinea, Samoa, Solomon Islands, Timor Leste, Tonga, Tuvalu\
                                 and Vanuatu. PaRIS was created by Applied GeoScience and Technology Division, \
                                 Secretariat of the Pacific Community (SOPAC).",
                    region="asiapacific",
                    screenshot="../static/img/paris.png",
                    screenshot_height=262,
                    url="http://paris.sopac.org",
                    )

virtual_kenya = GalleryItem("VirtualKenya.org",
                           "Upande Limied & WRI",
                           description="In 2011, a partnership was formed between <a href=\"http://www.upande.com/\"> \
                           Upande Limited</a> and <a href= \"http://www.wri.org/\">World Resources Institute</a> to \
                           jointly build <a href=\"http://maps.virtualkenya.org\">VirtualKenya.org</a> in to provide \
                           improved access to high quality spatial data and cutting-edge mapping technology. The goal \
                           of the system is to enable more Kenyans to use and interact with spatial data in their \
                           educational and professional pursuits.  VirtualKenya.org uses GeoNode to provide online\
                           access to publicly available spatial data sets and by offering users a number of \
                           interactive tools and learning resources for exploring these data.",
                           region="africa",
                           screenshot="../static/img/kenya.png",
                           screenshot_height=189,
                           url="http://maps.virtualkenya.org"
                           )

additional_geonodes = GalleryItem("More examples",
                                  "Links to additional GeoNode deployments.",
                                  description='<ul class="unstyled"> \
                                            <li><a href= "http://geonode.ithacaweb.org" target="_new">The CoSA Web Applicaiton</a> - Ithaca is using GeoNode as a demonstration of an online geospatial platform with data obtained through \
                                	         remote sensing techniques along with reference data to support the Post Disaster Needs Assessments.</li> \
                                            <li><a href= "http://www.golfgis.com" target="_new">Golfgis.com</a> - Golfgis.com was developed to help golf courses manage sustainably, reduce waste, improve ecological diversity and help drive business.</li>\
                                            <li><a href= "http://geonode.gov.vc" target="_new">St. Vincent Geonode</a> - Various ministries of the St. Vincent Government are using GeoNode to expose their geospatial data.</li>\
                                            <li><a href= "http://geonode.wfp.org" target="_new">World Food Programme</a> - The United Nations World Food Programme is using GeoNode enhance their data collecting capabilities from anywhere in the world. By leveraging features like on line editing features\
                                        and crowdsouring data they are be better prepared to react during humanitarian emergencies.</li> \
                                        </ul>',
                                  region='worldwide',
                                  screenshot="../static/img/additional.png"
                                  )

def preBuildPage(site, page, context, data):
        context['gallery'] = [bolivia, cba, cigno, haiti, mapstory, masdap, montagneAperte, mozadapt, paris,
                              virtual_kenya, additional_geonodes]
        return context, data
