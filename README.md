# Report
## Distributed Systems Lab 09

---

### 3 running

```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-31T17:07:52.786Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572541671, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-10-31T17:07:51.484Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572541671, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-31T17:07:51.484Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572541671, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572541671, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-10-31T17:07:51.484Z"),
		"lastDurableWallTime" : ISODate("2019-10-31T17:07:51.484Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572541661, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572541661, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-31T13:08:19.724Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572527295, 1),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572527295, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-31T13:08:21.062Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T13:08:22.081Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "db1.local:27017",
			"ip" : "172.31.30.96",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 11954,
			"optime" : {
				"ts" : Timestamp(1572541661, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572541661, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-31T17:07:41Z"),
			"optimeDurableDate" : ISODate("2019-10-31T17:07:41Z"),
			"lastHeartbeat" : ISODate("2019-10-31T17:07:51.300Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T17:07:51.913Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db3.local:27017",
			"syncSourceHost" : "db3.local:27017",
			"syncSourceId" : 2,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 1,
			"name" : "db2.local:27017",
			"ip" : "172.31.23.43",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 185904,
			"optime" : {
				"ts" : Timestamp(1572541671, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-31T17:07:51Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572527299, 1),
			"electionDate" : ISODate("2019-10-31T13:08:19Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "db3.local:27017",
			"ip" : "172.31.30.103",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 185323,
			"optime" : {
				"ts" : Timestamp(1572541671, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572541671, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-31T17:07:51Z"),
			"optimeDurableDate" : ISODate("2019-10-31T17:07:51Z"),
			"lastHeartbeat" : ISODate("2019-10-31T17:07:51.913Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T17:07:51.917Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db2.local:27017",
			"syncSourceHost" : "db2.local:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572541671, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572541671, 1)
}
```

```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "db1.local:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "db2.local:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "db3.local:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db840fc7d4ef60dba42bee7")
	}
}

```

![](https://i.imgur.com/DAL3Dpv.png)


### Primary died
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-31T17:56:11.688Z"),
	"myState" : 1,
	"term" : NumberLong(3),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"lastCommittedWallTime" : ISODate("2019-10-31T17:56:06.590Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-31T17:56:06.590Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"lastAppliedWallTime" : ISODate("2019-10-31T17:56:06.590Z"),
		"lastDurableWallTime" : ISODate("2019-10-31T17:56:06.590Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572544546, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572544546, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-31T17:54:45.213Z"),
		"termAtElection" : NumberLong(3),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572544481, 1),
			"t" : NumberLong(2)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572544481, 1),
			"t" : NumberLong(2)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 1,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-31T17:54:46.582Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T17:54:47.364Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "db1.local:27017",
			"ip" : "172.31.30.96",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 14858,
			"optime" : {
				"ts" : Timestamp(1572544566, 1),
				"t" : NumberLong(3)
			},
			"optimeDate" : ISODate("2019-10-31T17:56:06Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572544485, 1),
			"electionDate" : ISODate("2019-10-31T17:54:45Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "db2.local:27017",
			"ip" : "172.31.23.43",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-10-31T17:56:05.300Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T17:54:46.252Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to db2.local:27017 (172.31.23.43:27017) :: caused by :: No route to host",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 2,
			"name" : "db3.local:27017",
			"ip" : "172.31.30.103",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 14854,
			"optime" : {
				"ts" : Timestamp(1572544566, 1),
				"t" : NumberLong(3)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572544566, 1),
				"t" : NumberLong(3)
			},
			"optimeDate" : ISODate("2019-10-31T17:56:06Z"),
			"optimeDurableDate" : ISODate("2019-10-31T17:56:06Z"),
			"lastHeartbeat" : ISODate("2019-10-31T17:56:11.281Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T17:56:11.367Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db1.local:27017",
			"syncSourceHost" : "db1.local:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572544566, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572544566, 1)
}
```

```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-31T17:56:11.688Z"),
	"myState" : 1,
	"term" : NumberLong(3),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"lastCommittedWallTime" : ISODate("2019-10-31T17:56:06.590Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-31T17:56:06.590Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572544566, 1),
			"t" : NumberLong(3)
		},
		"lastAppliedWallTime" : ISODate("2019-10-31T17:56:06.590Z"),
		"lastDurableWallTime" : ISODate("2019-10-31T17:56:06.590Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572544546, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572544546, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-31T17:54:45.213Z"),
		"termAtElection" : NumberLong(3),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572544481, 1),
			"t" : NumberLong(2)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572544481, 1),
			"t" : NumberLong(2)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 1,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-31T17:54:46.582Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T17:54:47.364Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "db1.local:27017",
			"ip" : "172.31.30.96",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 14858,
			"optime" : {
				"ts" : Timestamp(1572544566, 1),
				"t" : NumberLong(3)
			},
			"optimeDate" : ISODate("2019-10-31T17:56:06Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572544485, 1),
			"electionDate" : ISODate("2019-10-31T17:54:45Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "db2.local:27017",
			"ip" : "172.31.23.43",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-10-31T17:56:05.300Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T17:54:46.252Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to db2.local:27017 (172.31.23.43:27017) :: caused by :: No route to host",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 2,
			"name" : "db3.local:27017",
			"ip" : "172.31.30.103",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 14854,
			"optime" : {
				"ts" : Timestamp(1572544566, 1),
				"t" : NumberLong(3)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572544566, 1),
				"t" : NumberLong(3)
			},
			"optimeDate" : ISODate("2019-10-31T17:56:06Z"),
			"optimeDurableDate" : ISODate("2019-10-31T17:56:06Z"),
			"lastHeartbeat" : ISODate("2019-10-31T17:56:11.281Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T17:56:11.367Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db1.local:27017",
			"syncSourceHost" : "db1.local:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572544566, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572544566, 1)
}
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "db1.local:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "db2.local:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "db3.local:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db840fc7d4ef60dba42bee7")
	}
}
```

![](https://i.imgur.com/7RwHUXP.png)
