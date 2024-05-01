if [ -z $1 ];
then
    echo "No database filename given!"
    exit 1
fi

docker cp $1 dspacedb:/db.sql
docker exec dspacedb /bin/bash -c "dropdb -U dspace dspace -f"
docker exec dspacedb /bin/bash -c "createdb -U dspace dspace"
docker exec dspacedb /bin/bash -c "psql -U dspace -d dspace < db.sql"
docker exec dspace /bin/bash -c "/dspace/bin/dspace index-discovery -b"

