cf. https://chezsoi.org/lucas/blog/visualisation-des-votes-sur-republique-numeriquefr

With a bit of dichotomy, the full IDs range of the /opinions resource on 2015/10/18 seems to be 61-782.

    for i in {61..782}; do
        curl --fail https://www.republique-numerique.fr/api/opinions/$i > opinions/$i.json || echo $i >> opinions_not_found
    done

    grep -l 'is_trashed":true' opinions/*


    echo "id,yes,no" > arguments_counts.csv
    cd opinions
    jq -r '.opinion|[(input_filename|split(".")[0]),.arguments_yes_count,.arguments_no_count]|@csv' *.json >> ../arguments_counts.csv
    cd ..

    $ jq '.opinion.arguments_yes_count' opinions/*.json | stats
    1-SUM      2-COUNT    3-MEAN     4-STD_DEV  5-MIN      6-TP01     7-TP10     8-MEDIAN   9-TP90     10-TP99    11-MAX    
    1960       696        2.81609    6.15793    0          0          0          1          7          33         78        
    $ jq '.opinion.arguments_no_count' opinions/*.json | stats
    1-SUM      2-COUNT    3-MEAN     4-STD_DEV  5-MIN      6-TP01     7-TP10     8-MEDIAN   9-TP90     10-TP99    11-MAX    
    2034       696        2.92241    6.73911    0          0          0          1          7          31         90        

    echo argument_votes_count,freq_yes,freq_no > arguments_counts_frequencies_histogram.csv
    python frequency_histogram.py arguments_counts.csv >> arguments_counts_frequencies_histogram.csv


    echo "id,ok,ko,mitige" > votes_counts.csv
    cd opinions
    jq -r '.opinion|[(input_filename|split(".")[0]),.votes_ok,.votes_nok,.votes_mitige]|@csv' *.json >> ../votes_counts.csv
    cd ..

    echo votes_count,freq_ok,freq_nok,freq_mitige > votes_counts_frequencies_histogram.csv
    python frequency_histogram.py votes_counts.csv | head -n 30 >> votes_counts_frequencies_histogram.csv
