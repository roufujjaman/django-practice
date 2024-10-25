from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = [
    "In the digital age, data security has become a critical concern for businesses and individuals alike. Protecting sensitive information, such as financial records and personal data, is essential to maintain trust and prevent fraud. Implementing robust security measures, including encryption and multi-factor authentication, helps safeguard data against potential threats and unauthorized access.",
    
    "Effective project management is essential for achieving success in any organization. It involves planning, organizing, and overseeing resources to accomplish specific goals within a set timeframe. Utilizing tools like Gantt charts, task management software, and regular communication can enhance team collaboration, streamline workflows, and ensure that projects are completed on time and within budget.",
    
    "Machine learning is a rapidly growing field within artificial intelligence that focuses on creating algorithms that can learn from data. By analyzing patterns, these algorithms can make predictions and decisions without explicit programming. Applications of machine learning range from natural language processing and image recognition to healthcare diagnostics and financial forecasting, transforming various industries.",
    
    "The evolution of technology has significantly impacted the way businesses operate. From automating repetitive tasks to enabling remote work, technological advancements have made processes more efficient and cost-effective. Companies that embrace innovation are better positioned to adapt to changes, improve productivity, and gain a competitive edge in the market.",
    
    "Sustainable architecture emphasizes the design of buildings that minimize environmental impact and maximize energy efficiency. By incorporating renewable energy sources, such as solar panels, and using eco-friendly materials, architects can create structures that are both functional and environmentally responsible. This approach promotes a healthier planet while also reducing operational costs over the building's lifespan."
]


def section(request, num):
    if 1 <= num <= 5:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")