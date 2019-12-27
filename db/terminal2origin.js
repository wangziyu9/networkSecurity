// 获取 ip_local 数量
db.origin.aggregate([      
    {"$match":{"ip_local": {$exists:true}}},   
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
            uname:x.uname,
            system:x.system,
            logdate:x.logdate,
            ip_server:x.ip_server,
            ip_local:x.ip_local,
            sizeOfip_local:x.sizeOfip_local
          }
    );
});