import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from lounge_app_services.employee.models import EmployeeLeave


def leave_type_chart(request):
    
    leaves = EmployeeLeave.objects.filter(employee__user__username=request.user)
    leave_data = [
        {'leave_type':leave.leave_type, 
         'no_of_days':leave.date_difference()+1,
         'leave_start_date':leave.leave_start_date,
         'leave_end_date':leave.leave_end_date,
         'is_approved':leave.is_approved}
         for leave in leaves
         ]
    
    df = pd.DataFrame.from_dict(data=leave_data)
    
    fig = px.bar(
        data_frame=df,
        y='no_of_days', 
        x='leave_type',
        color='leave_type', 
        title='Number of type of leaves', 
        labels={'leave_type':'Leave type', 'no_of_days':'No of Days'},
        )
     
    fig.update_layout(
        title={
        'font_size':22,
        'xanchor':'center',
        'x':0.5
        }   
    )
    return fig.to_html()