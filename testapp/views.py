from django.shortcuts import render

# Question class
class Questions:
    def __init__(self, que, a, b, c, d, correct, explanation):
        self.que = que
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct  # answer: 'a', 'b', 'c', 'd'
        self.explanation = explanation


def testpaper(request):
    questions = [
        Questions(
            'जीवों का वैज्ञानिक नाम किस भाषा में लिखा जाता है?',
            '(a) हिन्दी', '(b) अंग्रेज़ी', '(c) लैटिन', '(d) संस्कृत',
            'c',
            'वैज्ञानिक नाम सार्वभौमिक (Universal) होते हैं, इसलिए लैटिन भाषा का उपयोग किया जाता है।'
        ),

        Questions(
            'वैज्ञानिक नाम हमेशा किस रूप में लिखा जाता है?',
            '(a) दोनों शब्द बड़े अक्षरों में', '(b) दोनों शब्द छोटे अक्षरों में', '(c) प्रथम शब्द बड़ा, दूसरा छोटा', '(d) प्रथम शब्द छोटा, दूसरा बड़ा',
            'c',
            'पहला शब्द (Genus) → Capital letter दूसरा शब्द (Species) → Small letter ➡️ इसे Binomial Nomenclature कहते हैं।'
        ),

        Questions(
            'मनुष्य का वैज्ञानिक नाम क्या है?',
            '(a) Homo erectus', '(b) Homo sapiens', '(c) Panthera sapiens', '(d) Homo habilis',
            'b',
            'Species name sapiens का अर्थ है “wise man” (बुद्धिमान मनुष्य)।'
        ),

        Questions(
            'वैज्ञानिक नाम की खोज किसने की?',
            '(a) डार्विन', '(b) हुक', '(c) लिनियस', '(d) वॉटसन',
            'c',
            'Carolus Linnaeus ने द्वि-नाम पद्धति (Binomial Nomenclature) दी थी।'
        ),

        Questions(
            'Assertion (A):सभी वैज्ञानिक नाम लैटिन भाषा में लिखे जाते हैं। \
            Reason (R):लैटिन एक मृत भाषा है और समय के साथ बदलती नहीं है।',
            '(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या है', '(b) A और R दोनों सही हैं, पर R व्याख्या नहीं है', '(c) A सही है, R गलत है', '(d) A गलत है, R सही है',
            'a',
            'दोनों सही और R, A की व्याख्या करता है।'
        ),

        Questions(
            'Assertion (A):द्वि-नाम पद्धति में वैज्ञानिक नाम दो शब्दों का होता है। \
            Reason (R):पहला शब्द Species का नाम होता है।',
            '(a) A और R दोनों सही हैं तथा R, A की सही व्याख्या है', '(b) A और R दोनों सही हैं, पर R व्याख्या नहीं है', '(c) A सही है, R गलत है', '(d) A गलत है, R सही है',
            'c',
            'A सही है, पर R गलत है।'
        ),

        Questions(
            "Assertion (A): द्वि-नाम पद्धति में वैज्ञानिक नाम दो शब्दों से मिलकर बनता है.\n"
            "Reason (R): दूसरा शब्द Genus का नाम होता है.",

            "(a) दोनों सही और संबंधित", 
            "(b) A सही, R गलत", 
            "(c) दोनों गलत", 
            "(d) A गलत, R सही",

            "b",

            "Binomial nomenclature में वैज्ञानिक नाम दो शब्दों से बनता है—\n"
            "पहला शब्द = Genus\n"
            "दूसरा शब्द = Species\n"
            "लेकिन Reason (R) में कहा है कि दूसरा शब्द Genus का नाम होता है,\n"
            "जो गलत है। इसलिए A सही है लेकिन R गलत है।"
        ),

        Questions(
            "Assertion (A): मटर का वैज्ञानिक नाम Pisum sativum है।Reason (R): Gregor Mendel ने अनुवांशिकता के प्रयोग मटर पर किए थे।",
            
            "(a) दोनों सही और संबंधित",
            "(b) दोनों सही पर असंबंधित",
            "(c) A सही, R गलत",
            "(d) A गलत, R सही",
            
            "b",  
            
            "दोनों कथन सच हैं।"
            "A सही है क्योंकि मटर (garden pea) का वास्तविक वैज्ञानिक नाम Pisum sativum ही है।"
            "R भी सही है क्योंकि Gregor Mendel ने अपने सभी प्रसिद्ध आनुवंशिकी प्रयोग इसी पौधे पर किए थे।"
            "लेकिन R → A का कारण नहीं है। वैज्ञानिक नाम तो लिनियस ने 1753 में दे दिया था, जबकि मेंडल के प्रयोग 1856-1863 के बीच हुए।"
            "इसलिए दोनों कथन सही हैं लेकिन असंबंधित।"
            "सही उत्तर → (b)"
        ),


    ]

    # If student submits the test
    if request.method == "POST":
        score = 0
        detailed_result = []

        for i, q in enumerate(questions, 1):
            selected_option = request.POST.get(f'option{i}')

            if selected_option == q.correct:
                score += 1

            detailed_result.append({
                'question': q.que,
                'options': [q.a, q.b, q.c, q.d],
                'correct': q.correct,
                'selected': selected_option,
                'explanation': q.explanation
            })

        total = len(questions)
        percentage = round((score / total) * 100, 1)

        context = {
            'score': score,
            'total': total,
            'percentage': percentage,
            'result': detailed_result
        }
        return render(request, 'result.html', context)

    return render(request, 'question.html', {'questions': questions})
