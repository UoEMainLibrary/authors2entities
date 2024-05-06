if [ -z $1 ];
then
    echo "No database filename given!"
    exit 1
fi

docker exec dspacedb /bin/bash -c "pg_dump -U dspace > database_dump.sql"
docker cp   dspacedb:/database_dump.sql dumps/$1.sql
