{
  "targets": [
    {
      "target_name": "mpqtools",
      "sources": [ 
      	"mpqtools.cc", 
        "mpqtarchive.cc",
        "mpqtfile.cc"
      ],
      "link_settings": {
        "libraries": [
          "../StormLib/storm.framework/storm"
        ]
      }
    }
  ]
}