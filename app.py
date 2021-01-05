 #!/usr/bin/env python
 # -*-- coding: utf-8 -*--

#sonra diğer vt lerle bağlantı çalışması
#sonra da  vt üzerinden geonetwork e yazma denemesi
#bu olmazsa ki olmayabilir. http post


#içerik kontrolü yapılması lazım. 1 dalı doldurmadık henüz. ana tag kapanmamış. neden, ona bakmak lazım.
import os
import psycopg2 as pg
import configparser
import datetime
from xml.dom import minidom


try:
	config = configparser.ConfigParser()
	config.read(r'C:\Users\kemal.cenan\Desktop\xmlgen\xmlproject\config.env')
	cs = "dbname=%s user=%s password=%s host=%s port=%s" % (config.get('DB','DB_DATABASE'),config.get('DB','DB_USERNAME'),config.get('DB','DB_PASSWORD'),config.get('DB','DB_HOST'),config.get('DB','DB_PORT'))
	conn = pg.connect(cs)
	cur = conn.cursor()
	cur.execute('select * from metaveri_test')
	data=cur.fetchall()
	#organization mail kaç  adet girilecek bilgisi parametreden alınacak. şimdilik sayısal
	timedate = str(datetime.datetime.now())
	fname = timedate.replace('-','_')
	fname = fname.replace(':','')
	fname = (fname.replace(' ',''))[:16]
	timedate = timedate[:10]
	os.mkdir(fname)

	for i in data:
		if (i[0] is not None):
			print (i)
			guid = i[0]
			metaveri_adi = i[1]
			st_xmin = i[2]
			st_xmax = i[3]
			st_ymin = i[4]
			st_ymax = i[5]
			kw3 = i[6]
			kw4 = i[7]
			kw5 = i[8]
			ozet_metin = i[9]
			kurum_logo = i[10]
			online_resource = i[11]
			kisitlar = i[12]
			diger_kisitlar = i[13]
			kurum_adi = i[14]
			kurumsal_eposta = i[15]
			kurumsal_2eposta = i[16]
			kw1 = i[17]
			kw2 = i[18]
			sorumlu_eposta = i[19]
			sorumlu_2eposta = i[20]
			tucbs_katalog = i[21]
			servis_tipi = i[22]
			kaynak_tipi = i[23]
			baslik_kategorisi = i[24]
			yetki_tipi = i[25]
			Amac = i[26]
			Kullanim = i[27]
			Koken = i[28]
			Kaynaksema = i[29]
			Tanimlamadokumani = i[30]
			Eksiksizlik = i[31]
			Fazlalik = i[32]
			Eksiklik = i[33]
			Mantiksaltutarlilik = i[34]
			Kavramsaltutarlilik = i[35]
			Tanimkumesitutarlilik = i[36]
			Formattutarlilik = i[37]
			Topolojitutarlilik = i[38]
			Konumsaldogruluk = i[39]
			Mutlakdogruluk = i[40]
			Bagildogruluk = i[41]
			Rasterkonumdogruluk = i[42]
			Zamansaldogruluk = i[43]
			Ilgilizamandogruluk = i[44]
			Zamansaltutarlilik = i[45]
			Zamansalgecerlilik = i[46]
			Tematikdogruluk = i[47]
			Siniflandirmadogruluk = i[48]
			Niceloznitelikdogruluk = i[49]
			Nicelolmayanoznitelikdogruluk = i[50]
			root = minidom.Document()
			#kurumsal e-posta sayısı kadar child object eklenmesi için
			parameterOrgMail = 1
			mailOrg = []
			if i[15] is not None:
				parameterOrgMail = parameterOrgMail+1
				mailOrg.append(i[15])
			if i[16] is not None:
				parameterOrgMail = parameterOrgMail+1
				mailOrg.append(i[16])
			#sorumlu e-posta sayısı kadar child object eklenmesi için
			parameterResMail = 1
			mailRes = []
			if i[19] is not None:
				parameterResMail = parameterResMail+1
				mailRes.append(i[19])
			if i[20] is not None:
				parameterResMail = parameterResMail+1
				mailRes.append(i[20])
			#anahtar kelime sayısı kadar descriptiveKeywords tag i açılması için
			kwTotal = 1
			kwList = []
			if i[6] is not None:
				kwTotal = kwTotal+1
				kwList.append(i[6])
			if i[7] is not None:
				kwTotal = kwTotal+1
				kwList.append(i[7])
			if i[8] is not None:
				kwTotal = kwTotal+1
				kwList.append(i[8])
			if i[17] is not None:
				kwTotal = kwTotal+1
				kwList.append(i[17])
			if i[18] is not None:
				kwTotal = kwTotal+1
				kwList.append(i[18])


			#
			r1d = 'gmd:MD_Metadata'
			xml = root.createElement(r1d)
			r2d = 'xmlns:gmd'
			xml.setAttribute(r2d,'http://www.isotc211.org/2005/gmd')
			r3d='xmlns:srv'
			xml.setAttribute(r3d,'http://www.isotc211.org/2005/srv')
			r4d='xmlns:gco'
			xml.setAttribute(r4d, 'http://www.isotc211.org/2005/gco')
			r5d='xmlns:xsi'
			xml.setAttribute(r5d,'http://www.w3.org/2001/XMLSchema-instance')
			r6d='xmlns:gml'
			xml.setAttribute(r6d,'http://www.opengis.net/gml')
			r7d='xmlns:xlink'
			xml.setAttribute(r7d,'http://www.w3.org/1999/xlink')
			r8d='xsi:schemaLocation'
			xml.setAttribute(r8d,'http://www.isotc211.org/2005/gmd http://schemas.opengis.net/iso/19139/20060504/gmd/gmd.xsd')

			root.appendChild(xml)

			#burda tag lere başlıyoruz
			#tag 1
			productChild = root.createElement('gmd:fileIdentifier')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gco:CharacterString')
			childOfProduct.appendChild(root.createTextNode(str(guid)+'.xml'))
			productChild.appendChild(childOfProduct)


			#tag 2


			productChild = root.createElement('gmd:wfsRole')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gco:CharacterString')
			childOfProduct.appendChild(root.createTextNode(''))
			productChild.appendChild(childOfProduct)

			#tag 3

			productChild = root.createElement('gmd:organizationLogoUrl')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gco:CharacterString')
			childOfProduct.appendChild(root.createTextNode(kurum_logo))
			productChild.appendChild(childOfProduct)

			#tag 4


			productChild = root.createElement('gmd:wfsCatalog')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gco:CharacterString')
			childOfProduct.appendChild(root.createTextNode(str(tucbs_katalog)))
			productChild.appendChild(childOfProduct)

			#tag 5

			productChild = root.createElement('gmd:language')
			xml.appendChild(productChild)


			childOfProduct = root.createElement('gmd:LanguageCode')
			childOfProduct.setAttribute('codeListValue', 'tur')
			childOfProduct.setAttribute('codeList', 'http://www.loc.gov/standards/iso639-2/')
			childOfProduct.appendChild(root.createTextNode('tur'))
			productChild.appendChild(childOfProduct)

			#tag 6

			productChild = root.createElement('gmd:characterSet')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gmd:MD_CharacterSetCode')
			childOfProduct.setAttribute('codeListValue', 'utf8')
			childOfProduct.setAttribute('codeList', 'http://www.isotc211.org/2005/resources/codelist/gmxCodelists.xml#MD_CharacterSetCode')
			childOfProduct.setAttribute('codeSpace', 'ISOTC211/19115')
			childOfProduct.appendChild(root.createTextNode('utf8'))
			productChild.appendChild(childOfProduct)


			#tag 7

			productChild = root.createElement('gmd:hierarchyLevel')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gmd:MD_ScopeCode')
			childOfProduct.setAttribute('codeListValue', 'service')
			childOfProduct.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#MD_ScopeCode')
			childOfProduct.appendChild(root.createTextNode(kaynak_tipi))
			productChild.appendChild(childOfProduct)

			#buraya kadar sıkıntı yok. tek kırılım vardı ağaç yapısında. buradan sonra daha fazla budaklanma var.

			#tag 8

			productChild = root.createElement('gmd:contact')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gmd:CI_ResponsibleParty')
			productChild.appendChild(childOfProduct)

			#8in 1 daı
			subProductChild = root.createElement('gmd:organizationName')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gco:CharacterString')
			subSqProductChild.appendChild(root.createTextNode(kurum_adi))
			subProductChild.appendChild(subSqProductChild)

			#8in 2. dalı
			subProductChild = root.createElement('gmd:contactInfo')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:CI_Contact')
			subProductChild.appendChild(subSqProductChild)

			subCubProductChild = root.createElement('gmd:address')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:CI_Address')
			subCubProductChild.appendChild(subForthProductChild)


			for i in range(0,parameterOrgMail-1):

				subFifthProductChild = root.createElement('gmd:electronicMailAdress')
				subForthProductChild.appendChild(subFifthProductChild)

				subSixthProductChild = root.createElement('gco:CharacterString')
				subSixthProductChild.appendChild(root.createTextNode(mailOrg[i]))
				subFifthProductChild.appendChild(subSixthProductChild)


			#8in 3. dalı
			subProductChild = root.createElement('gmd:role')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:CI_RoleCole')
			subSqProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_RoleCode')
			subSqProductChild.setAttribute('codeListValue', yetki_tipi)
			subSqProductChild.appendChild(root.createTextNode(yetki_tipi))
			subProductChild.appendChild(subSqProductChild)
			childOfProduct.appendChild(subProductChild)


			#tag 9

			productChild = root.createElement('gmd:dateStamp')
			xml.appendChild(productChild)
			childOfProduct = root.createElement('gco:Date')
			childOfProduct.appendChild(root.createTextNode(timedate))
			productChild.appendChild(childOfProduct)

			#tag 10
			productChild = root.createElement('gmd:metadataStandardName')
			xml.appendChild(productChild)
			childOfProduct = root.createElement('gco:CharacterString')
			childOfProduct.appendChild(root.createTextNode('ISO19115'))
			productChild.appendChild(childOfProduct)

			#tag11

			productChild = root.createElement('gmd:metadataStandardVersion')
			xml.appendChild(productChild)
			childOfProduct = root.createElement('gco:CharacterString')
			childOfProduct.appendChild(root.createTextNode('2003/Cor.1:2006'))
			productChild.appendChild(childOfProduct)

			#tag 12
			#BURASI UZUN hikaye. en son bakalım

			productChild = root.createElement('gmd:identificationInfo')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('srv:SV_ServiceIdentification')
			productChild.appendChild(childOfProduct)

			#12.1
			subProductChild = root.createElement('gmd:citation')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:CI_Citation')
			subProductChild.appendChild(subSqProductChild)

			#12.1.1
			subCubProductChild = root.createElement('gmd:title')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gco:CharacterString')
			subForthProductChild.appendChild(root.createTextNode(metaveri_adi))
			subCubProductChild.appendChild(subForthProductChild)


			#12.1.2
			subCubProductChild = root.createElement('gmd:date')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:CI_Date')
			subCubProductChild.appendChild(subForthProductChild)
			#12.1.2.1
			subFifthProductChild = root.createElement('gmd:date')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:Date')
			subFifthProductChild.appendChild(subSixthProductChild)
			#12.1.2.2
			subFifthProductChild = root.createElement('gmd:dateType')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gmd:CI_DateTypeCode')
			subSixthProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode')
			subSixthProductChild.setAttribute('codeListValue', 'publication')
			subSixthProductChild.appendChild(root.createTextNode('publication'))
			subFifthProductChild.appendChild(subSixthProductChild)


			#12.1.3
			subCubProductChild = root.createElement('gmd:date')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:CI_Date')
			subCubProductChild.appendChild(subForthProductChild)
			#12.1.3.1
			subFifthProductChild = root.createElement('gmd:date')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:Date')
			subFifthProductChild.appendChild(subSixthProductChild)
			#12.1.3.2
			subFifthProductChild = root.createElement('gmd:dateType')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gmd:CI_DateTypeCode')
			subSixthProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode')
			subSixthProductChild.setAttribute('codeListValue', 'creation')
			subSixthProductChild.appendChild(root.createTextNode('creation'))
			subFifthProductChild.appendChild(subSixthProductChild)


			#12.1.4
			subCubProductChild = root.createElement('gmd:date')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:CI_Date')
			subCubProductChild.appendChild(subForthProductChild)
			#12.1.4.1
			subFifthProductChild = root.createElement('gmd:date')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:Date')
			subFifthProductChild.appendChild(subSixthProductChild)
			#12.1.4.2
			subFifthProductChild = root.createElement('gmd:dateType')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gmd:CI_DateTypeCode')
			subSixthProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode')
			subSixthProductChild.setAttribute('codeListValue', 'revision')
			subSixthProductChild.appendChild(root.createTextNode('revision'))
			subFifthProductChild.appendChild(subSixthProductChild)



			#12.2
			subProductChild = root.createElement('gmd:abstract')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gco:CharacterString')
			subSqProductChild.appendChild(root.createTextNode(ozet_metin))
			subProductChild.appendChild(subSqProductChild)




			#12.3
			subProductChild = root.createElement('gmd:pointOfContact')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:CI_ResponsibleParty')
			subProductChild.appendChild(subSqProductChild)

			#12.3.1
			subCubProductChild = root.createElement('gmd:organisationName')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gco:CharacterString')
			subForthProductChild.appendChild(root.createTextNode(kurum_adi))
			subCubProductChild.appendChild(subForthProductChild)


			#12.3.2
			subCubProductChild = root.createElement('gmd:contactInfo')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:CI_Contact')
			subCubProductChild.appendChild(subForthProductChild)

			subFifthProductChild = root.createElement('gmd:address')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gmd:CI_Address')
			subFifthProductChild.appendChild(subSixthProductChild)
			#12.3.2.1-n
			for i in range(0,parameterResMail-1):

				subSeventhProductChild = root.createElement('gmd:electronicMailAdress')
				subSixthProductChild.appendChild(subSeventhProductChild)

				subEighthProductChild = root.createElement('gco:CharacterString')
				subEighthProductChild.appendChild(root.createTextNode(mailRes[i]))
				subSeventhProductChild.appendChild(subEighthProductChild)

			#12.3.3

			subCubProductChild = root.createElement('gmd:role')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:CI_RoleCode')
			subForthProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_RoleCode')
			subForthProductChild.setAttribute('codeListValue', 'author')
			subForthProductChild.appendChild(root.createTextNode('author'))
			subCubProductChild.appendChild(subForthProductChild)


			#12.4 			kwTotal = 1  			kwList = []

			for k in range(0,kwTotal-1):

				subProductChild = root.createElement('gmd:descriptiveKeywords')
				childOfProduct.appendChild(subProductChild)

				subSqProductChild = root.createElement('gmd:MD_Keywords')
				subProductChild.appendChild(subSqProductChild)

				#12.4.1
				subCubProductChild = root.createElement('gmd:keyword')
				subSqProductChild.appendChild(subCubProductChild)

				subForthProductChild = root.createElement('gco:CharacterString')
				subForthProductChild.appendChild(root.createTextNode(kwList[k]))
				subCubProductChild.appendChild(subForthProductChild)

				#12.4.2
				subCubProductChild = root.createElement('gmd:thesaurusName')
				subSqProductChild.appendChild(subCubProductChild)

				subForthProductChild = root.createElement('gmd:CI_Citation')
				subCubProductChild.appendChild(subForthProductChild)
				#12.4.2.1
				subFifthProductChild = root.createElement('gmd:title')
				subForthProductChild.appendChild(subFifthProductChild)

				subSixthProductChild = root.createElement('gco:CharacterString')
				subSixthProductChild.appendChild(root.createTextNode(kwList[k]))
				subFifthProductChild.appendChild(subSixthProductChild)
				#12.4.2.2
				subFifthProductChild = root.createElement('gmd:date')
				subForthProductChild.appendChild(subFifthProductChild)

				subSixthProductChild = root.createElement('gmd:CI_Date')
				subFifthProductChild.appendChild(subSixthProductChild)
				#12.4.2.2.1
				subSeventhProductChild = root.createElement('gmd:date')
				subSixthProductChild.appendChild(subSeventhProductChild)

				subEighthProductChild = root.createElement('gco:Date')
				subEighthProductChild.appendChild(root.createTextNode(timedate))
				subSeventhProductChild.appendChild(subEighthProductChild)
				#12.4.2.2.2
				subSeventhProductChild = root.createElement('gmd:dateType')
				subSixthProductChild.appendChild(subSeventhProductChild)

				subEighthProductChild = root.createElement('gmd:CI_DateTypeCode')
				subEighthProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/Codelist/ML_gmxCodelists.xml#CI_DateTypeCode')
				subEighthProductChild.setAttribute('codeListValue', 'revision')
				subEighthProductChild.appendChild(root.createTextNode('revision'))
				subSeventhProductChild.appendChild(subEighthProductChild)











			#12.5
			subProductChild = root.createElement('gmd:resourceConstraints')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:MD_Constraints')
			subProductChild.appendChild(subSqProductChild)


			subCubProductChild = root.createElement('gmd:useLimitation')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gco:CharacterString')
			subForthProductChild.appendChild(root.createTextNode(kisitlar))
			subCubProductChild.appendChild(subForthProductChild)



			#12.6
			subProductChild = root.createElement('gmd:resourceConstraints')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:MD_LegalConstraints')
			subProductChild.appendChild(subSqProductChild)
			#12.6.1
			subCubProductChild = root.createElement('gmd:accessConstraints')
			subCubProductChild.setAttribute('codeListValue', 'otherConstraints')
			subCubProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#MD_RestrictionCode')
			subCubProductChild.appendChild(root.createTextNode(diger_kisitlar))
			subSqProductChild.appendChild(subCubProductChild)
			#12.6.2
			subCubProductChild = root.createElement('gmd:otherConstraints')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gco:CharacterString')
			subForthProductChild.appendChild(root.createTextNode(diger_kisitlar))
			subCubProductChild.appendChild(subForthProductChild)




			#12.7
			subProductChild = root.createElement('srv:serviceType')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gco:LocalName')
			subSqProductChild.appendChild(root.createTextNode('baslik_kategorisi'))
			subProductChild.appendChild(subSqProductChild)



			#12.8
			subProductChild = root.createElement('gmd:language')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:LanguageCode')
			subSqProductChild.setAttribute('codeList', 'http://www.loc.gov/standards/iso639-2/')
			subSqProductChild.setAttribute('codeListValue', 'tur')
			subSqProductChild.appendChild(root.createTextNode('tur'))
			subProductChild.appendChild(subSqProductChild)



			#12.9
			subProductChild = root.createElement('gmd:topicCategory')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:MD_TopicCategoryCode')
			subSqProductChild.appendChild(root.createTextNode('location'))
			subProductChild.appendChild(subSqProductChild)



			#12.10
			subProductChild = root.createElement('srv:extent')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:EX_Extent')
			subProductChild.appendChild(subSqProductChild)


			subCubProductChild = root.createElement('gmd:geographicElement')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:EX_GeographicBoundingBox')
			subCubProductChild.appendChild(subForthProductChild)

			#12.10.1
			subFifthProductChild = root.createElement('gmd:westBoundLongitude')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:Decimal')
			subSixthProductChild.appendChild(root.createTextNode(str(st_xmin)))
			subFifthProductChild.appendChild(subSixthProductChild)

			#12.10.2
			subFifthProductChild = root.createElement('gmd:eastBoundLongitude')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:Decimal')
			subSixthProductChild.appendChild(root.createTextNode(str(st_xmax)))
			subFifthProductChild.appendChild(subSixthProductChild)


			#12.10.3
			subFifthProductChild = root.createElement('gmd:southBoundLatitude')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:Decimal')
			subSixthProductChild.appendChild(root.createTextNode(str(st_ymin)))
			subFifthProductChild.appendChild(subSixthProductChild)


			#12.10.4
			subFifthProductChild = root.createElement('gmd:westBoundLongitude')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gmd:northBoundLatitude')
			subSixthProductChild.appendChild(root.createTextNode(str(st_ymax)))
			subFifthProductChild.appendChild(subSixthProductChild)


			#tag 13

			productChild = root.createElement('gmd:distributionInfo')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gmd:MD_Distribution')
			productChild.appendChild(childOfProduct)

			#branş 13.1

			subProductChild = root.createElement('gmd:distributionFormat')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:MD_Format')
			subProductChild.appendChild(subSqProductChild)


			subCubProductChild = root.createElement('gmd:name')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gco:CharacterString')
			subForthProductChild.appendChild(root.createTextNode('unknown'))
			subCubProductChild.appendChild(subForthProductChild)


			subCubProductChild = root.createElement('gmd:version')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gco:CharacterString')
			subForthProductChild.appendChild(root.createTextNode('unknown'))
			subCubProductChild.appendChild(subForthProductChild)

			#branş 13.2

			subProductChild = root.createElement('gmd:transferOptions')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:MD_DigitalTransferOptions')
			subProductChild.appendChild(subSqProductChild)


			subCubProductChild = root.createElement('gmd:onLine')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:CI_OnlineResource')
			subCubProductChild.appendChild(subForthProductChild)

			subFifthProductChild = root.createElement('gmd:linkage')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gmd:URL')
			subSixthProductChild.appendChild(root.createTextNode(online_resource))
			subFifthProductChild.appendChild(subSixthProductChild)



			#tag 14

			productChild = root.createElement('gmd:dataQualityInfo')
			xml.appendChild(productChild)

			childOfProduct = root.createElement('gmd:DQ_DataQuality')
			productChild.appendChild(childOfProduct)


			#14.1

			subProductChild = root.createElement('gmd:scope')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:DQ_Scope')
			subProductChild.appendChild(subSqProductChild)


			subCubProductChild = root.createElement('gmd:level')
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:MD_ScopeCode')
			subForthProductChild.setAttribute('codeList', 'http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#MD_ScopeCode')
			subForthProductChild.setAttribute('publication', 'publication')
			subForthProductChild.appendChild(root.createTextNode('publication'))
			subCubProductChild.appendChild(subForthProductChild)

			#14.2

			subProductChild = root.createElement('gmd:report')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:DQ_DomainConsistency')
			subSqProductChild.setAttribute('xsi:type','gmd:DQ_DomainConsistency_Type')
			subProductChild.appendChild(subSqProductChild)

			subCubProductChild = root.createElement('gmd:result',)
			subSqProductChild.appendChild(subCubProductChild)

			subForthProductChild = root.createElement('gmd:DQ_ConformanceResult')
			subForthProductChild.setAttribute('xsi:type','gmd:DQ_ConformanceResult_Type')
			subCubProductChild.appendChild(subForthProductChild)

			#14.2.1

			subFifthProductChild = root.createElement('gmd:specification')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gmd:CI_Citation')
			subFifthProductChild.appendChild(subSixthProductChild)

			#14.2.1.1

			subSeventhProductChild = root.createElement('gmd:title')
			subSixthProductChild.appendChild(subSeventhProductChild)

			subEighthProductChild = root.createElement('gco:CharacterString')
			subEighthProductChild.appendChild(root.createTextNode('location'))
			subSeventhProductChild.appendChild(subEighthProductChild)

			#14.2.1.2

			subSeventhProductChild = root.createElement('gmd:date')
			subSixthProductChild.appendChild(subSeventhProductChild)

			subEighthProductChild = root.createElement('gmd:CI_Date')
			subSeventhProductChild.appendChild(subEighthProductChild)

			#14.2.1.2.1

			subNinthProductChild = root.createElement('gmd:date')
			subEighthProductChild.appendChild(subNinthProductChild)

			subTenthProductChild = root.createElement('gco:date')
			subTenthProductChild.appendChild(root.createTextNode(timedate))
			subNinthProductChild.appendChild(subTenthProductChild)

			#14.2.1.2.2

			subNinthProductChild = root.createElement('gmd:dateType')
			subEighthProductChild.appendChild(subNinthProductChild)

			subTenthProductChild = root.createElement('gmd:CI_DateTypeCode ')
			subTenthProductChild.setAttribute('codeListValue','publication')
			subTenthProductChild.setAttribute('codeList','http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#CI_DateTypeCode')
			subTenthProductChild.appendChild(root.createTextNode('publication'))
			subNinthProductChild.appendChild(subTenthProductChild)


			#14.2.2
			subFifthProductChild = root.createElement('gmd:explanation')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:CharacterString')
			subSixthProductChild.appendChild(root.createTextNode('See the referenced specification'))
			subFifthProductChild.appendChild(subSixthProductChild)


			#14.2.3
			subFifthProductChild = root.createElement('gmd:pass')
			subForthProductChild.appendChild(subFifthProductChild)

			subSixthProductChild = root.createElement('gco:Boolean')
			subSixthProductChild.appendChild(root.createTextNode('true'))
			subFifthProductChild.appendChild(subSixthProductChild)

			#14.3

			subProductChild = root.createElement('gmd:lineage')
			childOfProduct.appendChild(subProductChild)

			subSqProductChild = root.createElement('gmd:LI_Lineage')
			subProductChild.appendChild(subSqProductChild)

			subCubProductChild = root.createElement('gmd:statement')
			subSqProductChild.appendChild(subCubProductChild)


			subForthProductChild = root.createElement('gco:CharacterString')
			subForthProductChild.appendChild(root.createTextNode('Amaç:['+str(Amac)+'] Kullanım: [' +str(Kullanim)+'] Verinin Kökeni: ['+str(Koken)+'] Kaynak Şeması: ['+str(Kaynaksema)+'] Tanımlama Dokümanı: ['+str(Tanimlamadokumani)+'] Verinin Eksiksizliği(Completeness) : ['+str(Eksiksizlik)+'] Fazlalık : ['+str(Fazlalik)+'] Eksiklik : ['+str(Eksiklik)+'] Mantıksal Tutarlılık(Logical Consistency) : ['+str(Mantiksaltutarlilik)+'] Kavramsal Tutarlılık : ['+str(Kavramsaltutarlilik)+'] Tanım Kümesi Tutarlılığı : ['+str(Tanimkumesitutarlilik)+'] Format Tutarlılığı[Test amaçlı üretildi.] '+str(Formattutarlilik)+'] Topoloji Tutarlılığı : ['+str(Topolojitutarlilik)+'] Konumsal Doğruluk(Positional Accuracy) : ['+str(Konumsaldogruluk)+'] Mutlak Doğruluk : ['+str(Mutlakdogruluk)+'] Bağıl Doruluk : ['+str(Bagildogruluk)+'] Raster Veri Konum Doğruluğu : ['+str(Rasterkonumdogruluk)+'] Zamansal Doğruluk(Temporal Accuracy) : ['+str(Zamansaldogruluk)+'] İlgili zamandaki doğruluk : ['+str(Ilgilizamandogruluk)+'] Zamansal tutarlılık : ['+str(Zamansaltutarlilik)+'] Zamansal geçerlilik : ['+str(Zamansalgecerlilik)+'] Tematik Doğruluk(Thematic Accuracy) : ['+str(Tematikdogruluk)+'] Sınıflandırma Doğruluğu : ['+str(Siniflandirmadogruluk)+'] Nicel öznitelik bilgilerinin doğruluğu : ['+str(Niceloznitelikdogruluk)+'] Nicel olmayan öznitelik bilgilerinin doğruluğu : ['+str(Nicelolmayanoznitelikdogruluk)+']'))
			subCubProductChild.appendChild(subForthProductChild)

	  #son






			xml_str = root.toprettyxml(indent="\t", encoding="UTF-8")

			save_path_file = fname+"/"+str(guid)+".xml"
			with open(save_path_file, "wb") as f:
				f.write(xml_str)

	pass
except Exception as e:
	raise
