#!/bin/bash

function create_directory {
    if [[ ! -d $1 ]] ; then
        mkdir -v $1
    fi
}

function download_audio {
   audio_extension=".mp3"
   base_uri="https://www.yoyochinese.com/audio/pychart/"

   pinyin_tone=1
   while [ $pinyin_tone -le 4 ]; do
      audio_uri="$base_uri$1$pinyin_tone$audio_extension"
      wget -v $audio_uri -P $2
      let pinyin_tone=$pinyin_tone+1
   done
}

function main {
    pinyin_file="pinyin_audio.txt"
#    echo $pinyin_file
    output_dir="../generated"

    create_directory $output_dir

    for i in $( cat $pinyin_file ); do
       download_audio $i $output_dir
    done
}

main > download_audio.log
