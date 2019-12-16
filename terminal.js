db.terminal.aggregate([
    {$group: {_id: "$ip_server",ip_local: {$push: "$ip_local"
            }
        }
    }
]).forEach(function(x){
    db.temp.insert(
          {
            ip_local: x.ip_local
          }
    );
});

// 取数组长度
db.terminal.aggregate([      
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
    db.temp1.insert(
          {
            uname:x.uname,
            system:x.system,
            logdate:x.logdate,
            ip_server:x.ip_server,
            ip_local:x.ip_local,
            sizeOfip_local:x.sizeOfip_local
          }
    );
});

// 去重
db.temp1.aggregate([
    {$group: {_id: {name:"$uname",ip_local:"$ip_local"},
        uname: {$push: "$uname"},
        system: {$push: "$system"},
        logdate: {$push: "$logdate"},
        ip_server: {$push: "$ip_server"},
        ip_local: {$push: "$ip_local"},
        sizeOfip_local: {$sum: "$sizeOfip_local"}
        }
    }
]).forEach(function(x){
    db.temp.insert(
          {
            uname:x.uname,
            system:x.system,
            logdate:x.logdate,
            ip_server:x.ip_server,
            ip_local:x.ip_local,
            sizeOfip_local:x.sizeOfip_local
          }
    );
});

// 去重
db.temp1.aggregate([
    {$group: {_id: {name:"$uname",ip_local:"$ip_local"},
        uname: {$push: "$uname"},
        system: {$push: "$system"},
        logdate: {$push: "$logdate"},
        ip_server: {$push: "$ip_server"},
        ip_local: {$push: "$ip_local"},
        sizeOfip_local: {$sum: "$sizeOfip_local"}
        },
        {$unwind:"$ip_local"}
    }
])