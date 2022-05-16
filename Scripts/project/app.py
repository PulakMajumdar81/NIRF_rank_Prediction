from flask import Flask,render_template,request
import rank



app=Flask(__name__)

@app.route("/")

def hello():
    return render_template("index.html")



@app.route("/sub", methods = ["POST"])
def submit():
    #Html to py
    if request.method =="POST":
        Nt=int(request.form["Nt"])
        Ne=int(request.form["Ne"])
        Np=int(request.form["Np"])
        Faculty_total=int(request.form["Faculty_total"])
        Faculty_PhD=int(request.form["Faculty_PhD"])
        Faculty_two_sem=int(request.form["Faculty_two_sem"])
        Faculty_8=int(request.form["Faculty_8"])
        Faculty_15=int(request.form["Faculty_15"])
        Faculty_16=int(request.form["Faculty_16"])
        FRU=float(request.form["FRU"])
        RP=float(request.form["RP"])

        First_intake=int(request.form["First_intake"])
        First_admit=int(request.form["First_admit"])
        First_graduate=int(request.form["First_graduate"])
        First_placed=int(request.form["First_placed"])
        First_higher=int(request.form["First_higher"])
        GMS=float(request.form["GMS"])
        GPHD=float(request.form["GPHD"])
        OI=float(request.form["OI"])
        PR=float(request.form["PR"])



    GPH=(40*(((First_placed+First_higher)/First_admit)))
    Ng=First_graduate/First_intake
    if ((Ng/80)*100) >1:
        GUE=15
    else :
        GUE=((Ng/80)*15*100) 

    GO=GUE+GPHD+GMS+GPH

    






    FSR=(450*Faculty_two_sem)/(Ne+Np)


    Fra=(Faculty_PhD)/Faculty_total
    Fq=0
    if Fra >.95:
        Fq=10
    else :
        Fq=(10*Fra)/(.95)
    
    F1=Faculty_8/Faculty_total
    F2=Faculty_15/Faculty_total
    F3=Faculty_16/Faculty_total

    if F1>1:
        F1=3
    else :
        F1=F1*3
    
    if F2>1:
        F2=3
    else :
        F2=F2*3

    if F3>1:
        F3=4
    else :
        F3=F3*4

    FQE=Fq+F1+F2+F3



    N=Nt+Np
    f_Nt_Ne=float(Ne/N)
    f_Np=float(Np/N)
    SS=f_Np*5+f_Nt_Ne*15


    TLR=(SS+FQE+FSR+FRU)

    NIRF=(TLR*0.3)+(PR*0.1)+RP*0.3+(GO*0.2)+(OI*0.1)
    nirf=('%.2f'%NIRF)
    Rank=rank.rank_prediction(NIRF)







    




    #py to html
    return render_template("sub.html",NIRF=nirf,rank=Rank)


if __name__ =="__main__":
    app.run(debug=True)