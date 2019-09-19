from jsonschema import validate, exceptions


schema = {
        "title": "Course",
        "type": "object",
        "required": ['id', 'name', 'phone', 'url', 'description', 'about',
                        'start_date', 'hascertification', 'status', 'category', 'slug'],
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string", "minLength": 8, "maxLength": 100},
            "slug": {"type": "string"},
            "category": {"type": "integer", "minimum": 1},
            "phone": {"type": "string", "pattern": "[0-9]"},
            "url": {"type": "string", "format": "url"},
            "description": {"type": "string"},
            "about": {"type": "string"},
            "start_date": {"type": "string", "format": "date"},
            "hascertification": {"type": "boolean"},
            "status": {"type": "boolean"}
          }
        }


try:
    validate(instance=
        # {"id": 20, "name": 0, "slug": "course20A", "category": 1, "phone": "344-44444",
        # "url": "http:\/\/127.0.0.1:8000\/admin\/courses", "description": "description Course", "about": "about Course",
        # "start_date": "2018-07-01", "hascertification": True, "status": True}

        {'id': 15, 'name': 'Course15A', 'slug': 'course15A', 'category': 1, 'phone': '34444444',
        'url': 'http://127.0.0.1:8000/admin/courses', 'description': 'description Course', 'about': 'about Course',
        'start_date': '2018-07-01', 'hascertification': True, 'status': True}
             , schema=schema)
except exceptions.ValidationError as e:
    print(f"Please check: {e.message}")
else:
    print("JSON OK")



