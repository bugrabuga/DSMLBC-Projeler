{\rtf1\ansi\ansicpg1254\cocoartf2578
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Customer Segmentation Using RFM (Recency, Frequency, Monetary)\
\
\uc0\u304 \u351  Problemi: Bir e-ticaret \u351 irketi m\'fc\u351 terilerini segmentlere ay\u305 r\u305 p bu segmentlere g\'f6re pazarlama stratejileri belirlemek istiyor.\
\
Veri Seti Hikayesi: online_retail_2 isimli veri seti \uc0\u304 ngiltere merkezli online bir sat\u305 \u351  ma\u287 azas\u305 n\u305 n 01/12/2009 - 09/12/2011 tarihleri aras\u305 ndaki sat\u305 \u351 lar\u305 n\u305  i\'e7erir. \u350 irketin \'fcr\'fcnleri hediyelik e\u351 yalar. \'c7o\u287 u m\'fc\u351 terinin toptanc\u305  oldu\u287 u bilgisi de mevcut.\
\
De\uc0\u287 i\u351 kenler:\
- InvoiceNo: Fatura numaras\uc0\u305 . Her fatura i\'e7in e\u351 siz numara, e\u287 er kod C ile ba\u351 l\u305 yorsa i\u351 lemin iptal edildi\u287 i anlam\u305 na gelir.\
- StockCode: \'dcr\'fcn kodu. Her \'fcr\'fcn i\'e7in e\uc0\u351 siz.\
- Description: \'dcr\'fcn ismi\
- Quantity: \'dcr\'fcn adedi. Faturadaki \'fcr\'fcnlerden ka\'e7ar tane sat\uc0\u305 ld\u305 \u287 \u305 n\u305  ifade eder.\
- InvoiceDate: Fatura tarihi\
- UnitPrice: \'dcr\'fcn fiyat\uc0\u305  (sterlin)\
- CustomerID: M\'fc\uc0\u351 teri numaras\u305 , her m\'fc\u351 teri i\'e7in e\u351 siz.\
- Country: M\'fc\uc0\u351 terinin ya\u351 ad\u305 \u287 \u305  \'fclke\
\
Ama\'e7: M\'fc\uc0\u351 terilerin davran\u305 \u351 lar\u305 n\u305 n tan\u305 mlanmas\u305  ve bu davran\u305 \u351 lardaki \'f6beklenmelere g\'f6re gruplar olu\u351 turulmak isteniyor. Ortak davran\u305 \u351 lar sergileyenler ayn\u305  gruplarda yer alacak ve bu gruplara \'f6zel pazarlama teknikleri geli\u351 tirilmesinde geri bildirimler yap\u305 lacak.\
\
\'97\'97\'97Veri Seti\'97\'97\'97\
online_retail_2.xlsx veri setine linkten ula\uc0\u351 abilirsiniz\
\pard\pardeftab720\partightenfactor0

\f1 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 https://archive.ics.uci.edu/ml/machine-learning-databases/00502/}