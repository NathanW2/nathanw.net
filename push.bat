fab publish
python C:\Python27\Scripts\s3cmd sync F:\nathanw.net\output/ s3://nathanw.net --acl-public --delete-removed --guess-mime-type 
