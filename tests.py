import json

from server import parseLookupResponse

res1 = """{
  "result" : {
    "version" : "1.2",
    "person" : {
      "cancelled" : false,
      "identifier" : {
        "scheme" : "crsid",
        "value" : "abcd1"
      },
      "displayName" : "Abcd Efg",
      "registeredName" : "A. Efg",
      "surname" : "Efg",
      "visibleName" : "Abcd Efg",
      "misAffiliation" : "student",
      "institutions" : [ {
        "cancelled" : false,
        "instid" : "EMMUG",
        "name" : "Emmanuel College - Undergraduates"
      } ],
      "staff" : false,
      "student" : true
    }
  }
}"""

res2 = """{
  "result" : {
    "version" : "1.2",
    "person" : {
      "cancelled" : true,
      "identifier" : {
        "scheme" : "crsid",
        "value" : "efg234"
      },
      "displayName" : "Efg Hijk",
      "registeredName" : "E.F. Hijk",
      "surname" : "Hijk",
      "visibleName" : "E.F. Hijk",
      "institutions" : [ ],
      "staff" : true,
      "student" : false
    }
  }
}"""

res3 = """{
  "result" : {
    "version" : "1.2",
    "person" : {
      "cancelled" : false,
      "identifier" : {
        "scheme" : "crsid",
        "value" : "lmn5"
      },
      "displayName" : "Lmn Opq",
      "registeredName" : "L. Opq",
      "surname" : "Opq",
      "visibleName" : "Lmn Opq",
      "misAffiliation" : "staff",
      "institutions" : [ {
        "cancelled" : false,
        "instid" : "ENG",
        "name" : "Department of Engineering"
      }, {
        "cancelled" : false,
        "instid" : "CHU",
        "name" : "Churchill College",
        "acronym" : "CHU"
      } ],
      "staff" : true,
      "student" : false
    }
  }
}"""

def test_active_student():
    assert parseLookupResponse(json.loads(res1)['result']) == {
        'crsid': 'abcd1',
        'displayName': 'Abcd Efg',
        'cancelled': False,
        'isStudent': True,
        'isStaff': False,
        'affiliation': 'student',
        'colleges': [{'id': 'EMMUG', 'name': 'Emmanuel College - Undergraduates'}]
    }

def test_cancelled_student():
    assert parseLookupResponse(json.loads(res2)['result']) == {
        'crsid': 'efg234',
        'displayName': 'Efg Hijk',
        'cancelled': True,
        'isStudent': False,
        'isStaff': True,
        'affiliation': '',
        'colleges': []
    }

def test_active_staff():
    assert parseLookupResponse(json.loads(res3)['result']) == {
        'crsid': 'lmn5',
        'displayName': 'Lmn Opq',
        'cancelled': False,
        'isStudent': False,
        'isStaff': True,
        'affiliation': 'staff',
        'colleges': [{'id': 'CHU', 'name': 'Churchill College'}]
    }