
// 去重
db.terminal.aggregate([
    {$group: {
        _id: {name:"$uname",ip_local:"$ip_local"},
        uname: {$push: "$uname"},
        system: {$push: "$system"},
        logdate: {$push: "$logdate"},
        ip_server: {$push: "$ip_server"},
        ip_local: {$push: "$ip_local"},
        },
    },
    {$unwind:"$ip_local"},
    {$unwind:"$ip_local"},
    {$group: {_id: "$_id",
        uname: {$first: "$uname"},
        system: {$first: "$system"},
        logdate: {$first: "$logdate"},
        ip_server: {$first: "$ip_server"},
        ip_local: {$addToSet: "$ip_local"},
        },
    },
],{ allowDiskUse: true } ).forEach(function(x){
    db.temp.insert(
        {
            uname:x.uname,
            system:x.system,
            logdate:x.logdate,
            ip_server:x.ip_server,
            ip_local:x.ip_local,
        }
    );
});
db.temp.aggregate([      
    {"$match":{"ip_local": {$exists:true}}   },   
    {"$project": {
        "_id":0,
        "system":1,
        "uname":1,  
        "logdate":1,
        "ip_server":1,
        "ip_local":1,
        "sizeOfip_local": {"$size": "$ip_local"}         
        }    
    }
]).forEach(function(x){
    db.target.insert(
          {
            uname:x.uname[0],
            system:x.system[0],
            logdate:x.logdate[0],
            ip_server:x.ip_server[0],
            ip_local:x.ip_local,
            sizeOfip_local:x.sizeOfip_local
          }
    );
});