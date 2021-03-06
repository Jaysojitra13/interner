from django import template
from intern.models import *
from company.models import *

register = template.Library()

@register.filter(name="intern_name") 
def intern_name(value):
	personalDetail = PersonalDetails.objects.filter(internprofile_id = value)
	return personalDetail

@register.filter(name="post_name")
def post_name(value):
	postDetail = PostDetails.objects.filter(id = value)
	return postDetail

@register.filter(name="academic_detail")
def academic_detail(value):
	academicDetail = AcademicDetails.objects.filter(internprofile_id = value)
	return academicDetail

@register.filter(name="project_detail")
def project_detail(value):
	projectDetail = ProjectDetails.objects.filter(internprofile_id = value)
	return projectDetail

@register.filter(name="upc_details")
def upc_details(value):
	upc_post = UserPostConnection.objects.get(postdetails_id = value)
	return upc_post.status

@register.filter(name="upc_detailss")
def upc_detailss(value):
	q4 = UserPostConnection.objects.get(id = value)
	return q4.status

