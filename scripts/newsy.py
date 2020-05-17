############################################################################
import publications
import processing

### set admin variables ###

now_stamp = processing.now_stamp()
archive_location = processing.archive_location(now_stamp)

## create archive location ###

processing.create_archive(archive_location)

### define instances of Publication class ###

publications = [publications.BBC, publications.Guardian, publications.Independent, publications.Mail, publications.Telegraph, publications.Times, publications.Sun]

# fetch and archive html for Publication instances

for publication in publications:
    publication.html = publication.fetch_html(publication.url)
    publication.store_html(publication, now_stamp, archive_location, '')
