from django.shortcuts import render

def contact(request):
    context = {
        'author': 'Shah Jalal',
        'age': 24,
        'gender': 'Male',
        'marks': 92,
        'courses': [
            {
                'id': 1,
                'course': 'C++',
                'teacher': 'Farabi'
            },
            {
                'id': 2,
                'course': 'Python Programming',
                'teacher': 'Shah Jalal'
            },
            {
                'id': 3,
                'course': 'Java Programming',
                'teacher': 'Abdul Karim'
            },
            {
                'id': 4,
                'course': '.NET Framework Development',
                'teacher': 'Shariq'
            },
            {
                'id': 5,
                'course': 'Web Designing with HTML and CSS',
                'teacher': 'Faruk Hasan'
            },
            {
                'id': 6,
                'course': 'Database Management System (DBMS)',
                'teacher': 'Md Shah Jalal'
            }
        ]
    }
    return render(request, './first_app/index.html', context)
