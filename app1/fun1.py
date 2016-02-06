from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,inch,landscape,A4
from reportlab.platypus import *#Image,Table,TableStyle,Paragraph,SimpleDocTemplate,Spacer
from reportlab.lib import colors,utils
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.graphics.shapes import *
from reportlab.graphics.shapes import Image
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.widgets.markers import makeMarker
def draw_line(c,x,y,leng,wid):
	c.line(x,y,leng,wid)
def basic_info(fn,ln,c):#elements):
	c.setStrokeColorRGB(1,0.1,0.1)
	draw_line(c,-1*inch,-1*inch,8*inch,-1*inch)
	draw_line(c,-1*inch,-1*inch,-1*inch,11*inch)
	draw_line(c,7.24*inch,-1*inch,7.24*inch,11*inch)
	draw_line(c,-1*inch,10.65*inch,7.24*inch,10.65*inch)
	user=User.objects.get(first_name=fn,last_name=ln)
	company=Company.objects.get(id=user.company_id)
	c.setFont('Helvetica',48,leading=None)
	c.drawCentredString(3*inch, 0*inch,fn+" "+ln+" info")
	dat=[]
	dat.append([])
	dat[0].append(str("First Name:"))
	dat[0].append(str(user.first_name))
	dat.append([])
	dat[1].append(str("Last Name:"))
	dat[1].append(str(user.last_name))
	dat.append([])
	dat[2].append(str("phone:"))
	dat[2].append(str(user.phone))
	dat.append([])
	dat[3].append(str("company name"))
	dat[3].append(str(company.name))
	styles = ParagraphStyle(
    name='Normal',
    fontName='Helvetica-Bold',
    fontSize=9,
	)
	data2=[[Paragraph(cell,styles) for cell in row] for row in dat]
	t=Table(data2,colWidths=None,rowHeights=None,splitByRow=False,hAlign="RIGHT")
	t.setStyle(TableStyle([('FONTSIZE', (0,0), (-1, -1), 800),
			 ('TEXTALIGN',(0,0),(-1,-1),'CENTER'),
			 ('TEXTCOLOR',(0,0),(-1,-1),colors.red),
	         ('VALIGN',(0,0),(-1,-1),'CENTER'),
	         ('ALIGN',(0,0),(-1,-1),'CENTER'),
	         #('TOPPADDING',(0,0),(-1,-1),10),
	         ('BOTTOMPADDING',(0,0),(-1,-1),12),
	         ('INNERGRID', (0,0), (-1,-1), 0.50, colors.black),
	         ('BOX', (0,0), (-1,-1), 0.50, colors.black),
             ('BACKGROUND',(0,0),(-1,-1),colors.white),
             ('LINEBEFORE',(1,0),(-1,-1),1,colors.pink),
            ]))
	t.wrapOn(c,0*inch,0*inch)
	t.drawOn(c,3*inch,0.5*inch)#[1.8,9.6]))
	c.setTitle(fn+" "+ln+" info")
	img=str(user.picture)
	c.saveState()
	c.rotate( 180 )
	c.scale(-1.0,1.0)
	c.drawImage(img,0*inch,-2.5*inch,width=1.5*inch,height=2*inch)#,mask='auto')
	c.restoreState()

	
def func(request):
	c=canvas.Canvas("fun.pdf",pagesize=A4,bottomup=0)
	c.translate(inch,inch)
	basic_info("ram","kumar",c)#,pagesize)
	c.save()
	return HttpResponse("Hello world.You'reat the polls index.")
