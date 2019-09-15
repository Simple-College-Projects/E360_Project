from flask import Flask,render_template,request,jsonify,session,flash,redirect
from db import connection
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "qwerty"
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg','png'])
api = Api(app)

CORS(app)


@app.route('/')
def home():
    return render_template("nlog.html")

@app.route('/addhotel')
def addhotel():
    return render_template("add_hotel.html")

@app.route('/adminhome')
def adminhome():
    return render_template("adminindex.html")



@app.route('/login')
def login():
    cm,con = connection()
    usr=request.args.get('un')
    pwd=request.args.get('pw')
    llo="SELECT * FROM login WHERE `username`='"+usr+"' AND `password`='"+pwd+"'"
    print(llo)
    cm.execute(llo)
    ab=cm.fetchone()
    if ab is not None:
        session['uid'] = ab[0];
        session['type'] = ab[3];
        return jsonify(status="ok",id=ab[0],type=ab[3])
    else:
        return jsonify(status="no")

@app.route('/manager_details')
def manager_details():
    cm,con = connection()
    memid = request.get('memid')
    cm.execute("SELECT image,f_name FROM employee WHERE emp_id='"+memid+"'")
    ab=cm.fetchone()
    return jsonify(status="ok",mname=ab[1],mimage=ab[0])

@app.route('/hotelreg',methods=['POST'])
def hotelreg():
    cm, con = connection()
    name = request.form['hotel']
    star = request.form['star']
    description = request.form['desc']
    address = request.form['address']
    Latitude = request.form['lati']
    Longitude = request.form['longi']
    contact = request.form['contact']
    Email = request.form['email']
    Website = request.form['website']

    photo = ""

    file = request.files['image']
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    photo = timestr + file.filename
    if file and allowed_file(photo):

        file.save(os.path.join(app.root_path, 'static/uploads/' + photo))
    else:
        flash('Only JPEG & JPG files allowed')
        redirect('addhotel')


    amenities=request.form.getlist('amenities[]')
    am="";
    if amenities is not None:
        for i in amenities:
            am+=i+","


    cm.execute("INSERT INTO hotel VALUES(NULL,'" + name + "','" + star + "','" + description + "','" + address + "','" + photo + "','" +am+ "','" + Latitude + "','" + Longitude + "','" + contact + "','" +Email + "','" + Website + "')")
    con.commit()
    return '''<script>alert("Registration successfull"); </script>'''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/viewhotels',methods=['GET'])
def viewhotels():
    cm,con = connection()
    r="SELECT * from hotel"
    cm.execute(r)
    ab=cm.fetchall()
    print(ab)
    row_header = [x[0] for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/edit_view',methods=['GET'])
def edit_view():
    cm,con = connection()
    id=request.args.get('id')
    r="SELECT * from hotel where id='"+id+"'"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/update_hotel',methods=['POST'])
def update_hotel():
    cm, con = connection()
    id = request.form['hid']
    name = request.form['hotel']
    star = request.form['star']
    description = request.form['desc']
    address = request.form['address']
    Latitude = request.form['lati']
    Longitude = request.form['longi']
    contact = request.form['contact']
    Email = request.form['email']
    Website = request.form['website']

    amenities=request.form.getlist('amenities[]')
    am="";
    if amenities is not None:
        for i in amenities:
            am+=i+","
    cm.execute("UPDATE hotel set name='"+name+"', star='"+star+"',description='"+description+"',address='"+address+"',ameneties='"+am+"',latitude='"+Latitude+"',longtitude='"+Longitude+"',contact='"+contact+"',email='"+Email+"',website='"+Website+"' WHERE `id`='"+id+"'")
    con.commit()
    return '''<script>alert("Updated successfully"); </script>'''


@app.route('/delete_hotel',methods=['POST'])
def delete_hotel():
    cm,con = connection()
    id = request.form['id']
    try:
        cm.execute("DELETE FROM hotel WHERE `id`='"+str(id)+"'")
        con.commit()
        return jsonify(success="ok")
    except Exception as e:
        return jsonify(success="no")

@app.route('/view_hotel',methods=['GET'])
def view_hotel():
    cm,con = connection()
    r="SELECT * FROM hotel"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0] for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/deptreg',methods=['POST'])
def deptreg():
    cm, con = connection()
    dname = request.form['department']
    hotel_id = request.form['hotel_id']
    cm.execute("INSERT INTO `department`(`department`,`hotel_id`)VALUES ('"+dname+"','"+hotel_id+"')")
    con.commit()
    return '''<script>alert("Registration successfull"); </script>'''


@app.route('/view_dept',methods=['GET'])
def view_dept():
    cm,con = connection()
    r="SELECT `department`.`department`,`department`.`id`,`hotel`.`name` FROM `department`,`hotel` WHERE `department`.`hotel_id`=`hotel`.`id`"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0] for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/edit_dept_view',methods=['GET'])
def edit_dept_view():
    cm,con = connection()
    id=request.args.get('id')
    r="SELECT `department`.`department`,`department`.`id`,`hotel`.`name`,`hotel`.`id` AS hotel_id FROM `department`,`hotel` WHERE `department`.`hotel_id`=`hotel`.`id` AND `department`.`id`='"+id+"'"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/update_department',methods=['POST'])
def update_department():
    cm, con = connection()
    id = request.form['did']
    dname = request.form['department']
    hotel_id = request.form['hotel_id']
    cm.execute("UPDATE `department` SET `department`='"+dname+"',`hotel_id`='"+hotel_id+"' WHERE `id`='"+id+"'")
    con.commit()
    return '''<script>alert("Updated successfully"); </script>'''

@app.route('/delete_dept',methods=['POST'])
def delete_dept():
    cm,con = connection()
    id = request.form['id']
    try:
        cm.execute("DELETE FROM `department` WHERE `id`='" + str(id) + "'")
        con.commit()
        return jsonify(success="ok")
    except Exception as e:
        return jsonify(success="no")


@app.route('/select_dept_view',methods=['GET'])
def select_dept_view():
    cm,con = connection()
    id=request.args.get('id')
    r="SELECT `department`.`department`,`department`.`id` FROM `department` WHERE `department`.`hotel_id`='"+str(id)+"'"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})



@app.route( '/employeereg', methods=['POST'] )
def employeereg():

        cm, con = connection()
        fname = request.form['fname']
        lname = request.form['lname']
        hotel = request.form['hotel']
        dept = request.form['de']
        jobp = request.form['jobpos']
        imei = request.form['imei']
        geder = request.form['gender']
        contact = request.form['phone']
        Email = request.form['email']
        marry = request.form['marr']
        dob = request.form['dob']
        addr = request.form['address']
        pEmail = request.form['pmail']
        pmob = request.form['pmobile']
        uname = request.form['uname']
        pname = request.form['pass']
        file = request.files['image']
        timestr = datetime.now().strftime( "%Y%m%d-%H%M%S" )
        photo = timestr + file.filename
        print("uname",uname)
        print("pass",pname)

        q = "SELECT * FROM login where username='"+uname+"' and password='"+pname+"'"
        cm.execute(q)
        bc = cm.fetchone()
        print("res",bc)
        if bc is not None:
            return '''<script>alert("Username and Password already exist"); </script>'''

        else:
            r = "SELECT * FROM `employee` WHERE `hotel_id`='" + hotel + "' AND `dept_id`='" + dept + "' AND `jop_position`='"+jobp+"' and `jop_position`='Manager'"
            cm.execute(r)
            ab = cm.fetchone()
            print("res1",ab)
            if ab is not None:
                return '''<script>alert("Manager already assigned.."); </script>'''

            else:
                if file and allowed_file(photo):

                    file.save(os.path.join(app.root_path, 'static/uploads/' + photo))
                else:
                    flash('Only JPEG & JPG files allowed')
                    redirect('addhotel')
                cm.execute(
                    "INSERT INTO login VALUES(NULL,'" + uname + "','" + pname + "','" + jobp + "')")
                id = con.insert_id();
                cm.execute("INSERT INTO employee VALUES('" + str(
                    id) + "','" + fname + "','" + lname + "','" + hotel + "','" + dept + "','" + jobp + "','" + Email + "','" + contact + "','" + imei + "','" + geder + "','" + marry + "','" + dob + "','" + addr + "','" + pEmail + "','" + pmob + "','" + photo + "')")
                con.commit()
                return '''<script>alert("Registration successfull"); </script>'''





@app.route('/view_employee',methods=['GET'])
def view_employee():
    cm,con = connection()
    r="SELECT `employee`.*,`hotel`.`name`,`department`.`department` FROM `employee`,`department`,`hotel` WHERE `employee`.`dept_id`=`department`.`id` AND `employee`.`hotel_id`=`hotel`.`id`"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0] for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/edit_emp_view',methods=['GET'])
def edit_emp_view():
    cm,con = connection()
    id=request.args.get('id')
    r="SELECT `employee`.*,`hotel`.`name`,`department`.`department` FROM `hotel`,`department`,`employee` WHERE `emp_id` = '"+id+"' AND `employee`.`hotel_id`=`hotel`.`id` AND `employee`.`dept_id`=`department`.`id`"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/update_employee',methods=['POST'])
def update_employee():
    cm, con = connection()
    id = request.form['emp_id']
    fname = request.form['fname']
    lname = request.form['lname']
    imei = request.form['imei']
    geder = request.form['gender']
    contact = request.form['phone']
    Email = request.form['email']
    marry = request.form['marr']
    dob = request.form['dob']
    addr = request.form['address']
    pEmail = request.form['pmail']
    pmob = request.form['pmobile']
    cm.execute("UPDATE employee SET `f_name`='"+fname+"',`l_name`='"+lname+"',`work_email`='"+Email+"',`work_mob`='"+contact+"',`work_imei`='"+imei+"',`gender`='"+geder+"',`marital_status`='"+marry+"',`dob`='"+dob+"',`address`='"+addr+"',`pmail`='"+pEmail+"',`pmobile`='"+pmob+"' WHERE emp_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("Updated successfully"); </script>'''


@app.route('/delete_employees',methods=['POST'])
def delete_employees():
    cm,con = connection()
    id = request.form['id']
    try:
        cm.execute("DELETE FROM employee WHERE emp_id='"+str(id)+"'")
        con.commit()
        return jsonify(success="ok")
    except Exception as e:
        return jsonify(success="no")


@app.route('/member_view',methods=['GET'])
def member_view():
    cm,con = connection()
    mid=request.args.get('memid')
    r="SELECT `dept_id` FROM `employee` WHERE `employee`.`emp_id`='"+str(mid)+"'"
    cm.execute(r)
    ab=cm.fetchone()
    q = "SELECT `f_name`,`l_name`,`emp_id` FROM `employee`,`login` WHERE `employee`.`emp_id`=`login`.`id` AND `login`.`type`='Employee' AND `employee`.`dept_id`='" + str(ab[0]) + "'"
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/eventreg',methods=['POST'])
def eventreg():
    cm, con = connection()
    event = request.form['ename']
    description = request.form['edesc']
    event_date = request.form['edate']
    location = request.form['eloc']
    client = request.form['client']
    address = request.form['addr']
    quantity = request.form['quan']
    member_id = request.form['memid']
    cm.execute("INSERT INTO event VALUES(NULL,'" + event + "','" + description + "','" + event_date + "','" + location + "','" +client+ "','" + address + "','" + quantity + "','" + str( member_id) + "')")
    event_id=con.insert_id()
    members = request.form.getlist('members[]')
    mem = "";
    if members is not None:
        for i in members:
            cm.execute("INSERT INTO event_employee VALUES(NULL,'" + str(event_id) + "','" + str(i) + "')")
    con.commit()
    return '''<script>alert("Registration successfull"); </script>'''


@app.route('/viewevents',methods=['GET'])
def viewevents():
    cm,con = connection()
    mid=request.args.get('memid')
    q = "select * from event where manager_id='" + str(mid) + "'"
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/member_pop_view',methods=['GET'])
def member_pop_view():
    cm,con = connection()
    eid=request.args.get('eventid')
    q = "SELECT `f_name`,`l_name` FROM `employee`,`event_employee` WHERE `employee`.`emp_id`=`event_employee`.`employee_id` AND `event_employee`.`event_id`='" + str(eid) + "'"
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/event_edit_view',methods=['GET'])
def event_edit_view():
    cm,con = connection()
    id=request.args.get('id')
    r="SELECT * from event where id='"+id+"'"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0] for x in cm.description]
    q = "SELECT `event_employee`.employee_id FROM `event`,`event_employee` WHERE `event`.id='"+id+"' AND `event`.id=`event_employee`.event_id"
    cm.execute(q)
    bc = cm.fetchall()
    row_header1 = [y[0] for y in cm.description]
    json_data = []
    json_data1 = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    for result1 in bc:
        json_data1.append(dict(zip(row_header1, result1)))
    return jsonify({"success":json_data,"member":json_data1})


@app.route('/update_events',methods=['POST'])
def update_events():
    cm, con = connection()
    id = request.form['eventid']
    event = request.form['ename']
    description = request.form['edesc']
    event_date = request.form['edate']
    location = request.form['eloc']
    client = request.form['client']
    address = request.form['addr']
    quantity = request.form['quan']
    cm.execute("UPDATE `event` SET `event_name`='"+event+"',`description`='"+description+"',`event_date`='"+event_date+"',`event_location`='"+location+"',`client_name`='"+client+"',`address`='"+address+"',`quantity`='"+quantity+"' WHERE id='"+str(id)+"'")
    cm.execute("DELETE from `event_employee` where event_id='"+str(id)+"'")
    members = request.form.getlist('members[]')
    mem = "";
    if members is not None:
        for i in members:
            cm.execute("INSERT INTO event_employee VALUES(NULL,'" + str(id) + "','" + str(i) + "')")
    con.commit()

    return '''<script>alert("Updated successfully"); </script>'''


@app.route('/delete_event',methods=['POST'])
def delete_event():
    cm,con = connection()
    id = request.form['id']
    try:
        cm.execute("DELETE FROM event WHERE id='"+str(id)+"'")
        con.commit()
        return jsonify(success="ok")
    except Exception as e:
        return jsonify(success="no")

@app.route('/taskreg',methods=['POST'])
def taskreg():
    cm, con = connection()
    eid = request.form['eid']
    tname = request.form['tname']
    tdesc = request.form['tdesc']
    cm.execute("INSERT INTO `task` VALUES(NULL,'"+eid+"','"+tname+"','"+tdesc+"')")
    con.commit()
    return '''<script>alert("Registration successfull"); </script>'''


@app.route('/viewtask',methods=['GET'])
def viewtask():
    cm,con = connection()
    mid = request.args.get('memid')
    r="SELECT task.*,event.event_name,event_date,event_location,client_name FROM `task`,`event` WHERE `event`.`manager_id`='"+mid+"' AND `event`.`id`=`task`.`event_id`"
    cm.execute(r)
    ab=cm.fetchall()
    print(ab)
    row_header = [x[0] for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/delete_task',methods=['POST'])
def delete_task():
    cm,con = connection()
    id = request.form['id']
    try:
        cm.execute("DELETE FROM task WHERE id='"+str(id)+"'")
        con.commit()
        return jsonify(success="ok")
    except Exception as e:
        return jsonify(success="no")

@app.route('/task_edit_view',methods=['GET'])
def task_edit_view():
    cm,con = connection()
    id=request.args.get('id')
    r="SELECT * FROM `task` WHERE id = '"+id+"'"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/update_task',methods=['POST'])
def update_task():
    cm, con = connection()
    tid = request.form['tid']
    eid = request.form['eid']
    tname = request.form['tname']
    tdesc = request.form['tdesc']
    cm.execute("UPDATE task SET event_id='"+eid+"',task='"+tname+"',description='"+tdesc+"' where id='"+str(tid)+"'")
    con.commit()
    return '''<script>alert("Updated successfully"); </script>'''

@app.route('/assign',methods=['POST'])
def assign():
    cm, con = connection()
    eid = request.form['eid']
    tid = request.form['tid']
    empid = request.form['empid']
    estimate=request.form['est']
    priority = request.form['prior']
    cm.execute("INSERT INTO assign VALUES(NULL,'"+eid+"','"+tid+"','"+empid+"','"+estimate+"','pending','"+priority+"','new','pending','pending')")
    con.commit()
    return '''<script>alert("Registration successfull"); </script>'''


@app.route('/view_task_emp',methods=['GET'])
def view_task_emp():
    cm,con = connection()
    eid=request.args.get('eventid')
    r="select id,task from task where event_id='"+eid+"'"
    cm.execute(r)
    ab=cm.fetchall()
    row_header = [x[0] for x in cm.description]
    q = "SELECT `employee`.`emp_id`,`f_name`,`l_name` FROM`employee`,`event_employee` WHERE `event_employee`.`event_id`='"+eid+"' AND `event_employee`.`employee_id`=`employee`.`emp_id`"
    cm.execute(q)
    bc = cm.fetchall()
    row_header1 = [y[0] for y in cm.description]
    json_data = []
    json_data1 = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    for result1 in bc:
        json_data1.append(dict(zip(row_header1, result1)))
    return jsonify({"success":json_data,"member":json_data1})


@app.route('/viewassign',methods=['GET'])
def viewassign():
    cm,con = connection()
    mid = request.args.get('memid')
    r="SELECT `assign`.*,`employee`.`f_name`,`employee`.`l_name`,`event`.event_name,`task`.`task` FROM `assign`,`event`,`task`,`employee` WHERE `assign`.event_id=`event`.id AND `assign`.task_id=`task`.id AND `assign`.employee_id=`employee`.emp_id AND `event`.manager_id='"+mid+"'"
    cm.execute(r)
    ab=cm.fetchall()
    print(ab)
    row_header = [x[0] for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/delete_assign',methods=['POST'])
def delete_assign():
    cm,con = connection()
    id = request.form['id']
    try:
        cm.execute("DELETE FROM assign WHERE aid='"+str(id)+"'")
        con.commit()
        return jsonify(success="ok")
    except Exception as e:
        return jsonify(success="no")

@app.route('/assign_edit_view',methods=['GET'])
def assign_edit_view():
    cm,con = connection()
    id=request.args.get('id')
    r="SELECT * FROM assign WHERE aid = '"+id+"'"
    cm.execute(r)
    ab=cm.fetchall()
    print("dd",ab)
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in ab:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/update_assign',methods=['POST'])
def update_assign():
    cm, con = connection()
    aid = request.form['assid']
    eid = request.form['eid']
    tid = request.form['tid']
    empid = request.form['empid']
    estimate = request.form['est']
    priority = request.form['prior']
    cm.execute("UPDATE assign SET event_id='"+eid+"',task_id='"+tid+"',employee_id='"+empid+"',estimation='"+estimate+"',priority='"+priority+"' where aid='"+str(aid)+"'")
    con.commit()
    return '''<script>alert("Updated successfully"); </script>'''


@app.route('/view_emp_track',methods=['GET'])
def view_emp_track():
    cm,con = connection()
    mid=request.args.get('memid')
    r="SELECT `dept_id` FROM `employee` WHERE `employee`.`emp_id`='"+str(mid)+"'"
    cm.execute(r)
    ab=cm.fetchone()
    q = "SELECT employee.* FROM `employee`,`login` WHERE `employee`.`emp_id`=`login`.`id` AND `login`.`type`='Employee' AND `employee`.`dept_id`='" + str(ab[0]) + "'"
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/view_tracking',methods=['GET'])
def view_tracking():
    cm,con = connection()
    eid=request.args.get('empid')
    type = request.args.get('type')
    if type=="call":
        q = "SELECT * FROM `call` where emp_id='" + str(eid) + "'"
        cm.execute(q)
        bc = cm.fetchall()
        row_header = [x[0] for x in cm.description]
        json_data = []
        for result in bc:
            json_data.append(dict(zip(row_header, result)))
        return jsonify({"success": json_data})
    elif type=="message":
        q = "SELECT * FROM `message` where empid='" + str(eid) + "'"
        cm.execute(q)
        bc = cm.fetchall()
        row_header = [x[0] for x in cm.description]
        json_data = []
        for result in bc:
            json_data.append(dict(zip(row_header, result)))
        return jsonify({"success": json_data})
    else:
        return jsonify({"success": "no"})



@app.route('/count_history',methods=['GET'])
def count_history():
    cm,con = connection()
    eid=request.args.get('empid')
    r="SELECT COUNT(`browse`.id) FROM `browse` WHERE emp_id='"+eid+"'"
    cm.execute(r)
    ab=cm.fetchone()
    q = "SELECT COUNT(`call`.id) FROM `call` WHERE emp_id='"+eid+"'"
    cm.execute(q)
    bc = cm.fetchone()
    s = "SELECT COUNT(`message`.id) FROM `message` WHERE empid='" + eid + "'"
    cm.execute(s)
    cd = cm.fetchone()
    t = "SELECT COUNT(`location`.id) FROM `location` WHERE emp_id='" + eid + "'"
    cm.execute(t)
    de = cm.fetchone()
    return jsonify({"browse":ab[0],"call":bc[0],"message":cd[0],"location":de[0]})

@app.route('/count_details',methods=['GET'])
def count_details():
    cm,con = connection()
    r="SELECT COUNT(`id`) FROM `hotel`"
    cm.execute(r)
    ab=cm.fetchone()
    q = "SELECT COUNT(`id`) FROM `department`"
    cm.execute(q)
    bc = cm.fetchone()
    s = "SELECT COUNT(`emp_id`) FROM `employee`"
    cm.execute(s)
    cd = cm.fetchone()
    return jsonify({"hotel":ab[0],"department":bc[0],"employee":cd[0]})

@app.route('/task_report_view_admin',methods=['GET'])
def task_report_view_admin():
    cm,con = connection()
    fdate = request.args.get( 'sdate' )
    tdate = request.args.get( 'edate' )
    print(fdate)
    print(tdate)
    q = "SELECT `event`.`event_name`,`event`.`event_location`,`event`.`client_name`,a1.`f_name`,a1.`l_name` ,a1.`image`,`task`.`task`, `assign`.`estimation`,`assign`.`duration`,`assign`.`status`,`assign`.`task_date`,hotel.name, a2.f_name AS man_name FROM `assign`,`employee` AS a1,`employee` AS a2,`event`,`task`,hotel WHERE  a1.emp_id=`assign`.`employee_id` AND `event`.`id`=`task`.`event_id` AND `task`.`id`=`assign`.`task_id` AND hotel.id=a1.hotel_id AND a2.`jop_position`='Manager' AND a1.`jop_position`='Employee' AND a1.`dept_id`=a2.`dept_id` and  assign.task_date between '"+str(fdate)+"' and '"+str(tdate)+"'"
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/admin_task_report',methods=['GET'])
def admin_task_report():
    cm,con = connection()
    fdate = request.args.get( 'sdate' )
    tdate = request.args.get( 'edate' )

    q = "SELECT `event`.`event_name`,`event`.`event_location`,`event`.`client_name`,a1.`f_name`,a1.`l_name` ,a1.`image`,`task`.`task`, `assign`.`estimation`,`assign`.`duration`,`assign`.`status`,`assign`.`task_date`,hotel.name, a2.f_name AS man_name FROM `assign`,`employee` AS a1,`employee` AS a2,`event`,`task`,hotel WHERE  a1.emp_id=`assign`.`employee_id` AND `event`.`id`=`task`.`event_id` AND `task`.`id`=`assign`.`task_id` AND hotel.id=a1.hotel_id AND a2.`jop_position`='Manager' AND a1.`jop_position`='Employee' AND a1.`dept_id`=a2.`dept_id` and  assign.task_date between '"+str(fdate)+"' and '"+str(tdate)+"'"
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/task_report_view_admin_year',methods=['GET'])
def task_report_view_admin_year():
    cm,con = connection()
    year=request.args.get('year')
    print(year)
    q = "SELECT `event`.`event_name`,`event`.`event_location`,`event`.`client_name`,a1.`f_name`,a1.`l_name` ,a1.`image`,`task`.`task`, `assign`.`estimation`,`assign`.`duration`,`assign`.`status`,`assign`.`task_date`,hotel.name, a2.f_name AS man_name FROM `assign`,`employee` AS a1,`employee` AS a2,`event`,`task`,hotel WHERE  a1.emp_id=`assign`.`employee_id` AND `event`.`id`=`task`.`event_id` AND `task`.`id`=`assign`.`task_id` AND hotel.id=a1.hotel_id AND a2.`jop_position`='Manager' AND a1.`jop_position`='Employee' AND a1.`dept_id`=a2.`dept_id` AND  assign.task_date and year(assign.task_date)='" + year + "' "
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


@app.route('/task_report_view',methods=['GET'])
def task_report_view():
    cm,con = connection()
    mid=request.args.get('memid')
    r="SELECT `dept_id` FROM `employee` WHERE `employee`.`emp_id`='"+str(mid)+"'"
    cm.execute(r)
    ab=cm.fetchone()
    q = "SELECT `event`.`event_name`,`event`.`event_location`,`event`.`client_name`,`employee`.`f_name`,`employee`.`l_name` ,`employee`.`image`,`task`.`task`, `assign`.`estimation`,`assign`.`duration`,`assign`.`status` FROM `assign`,`employee`,`event`,`task` WHERE  `employee`.dept_id='"+str(ab[0])+"' AND `employee`.emp_id=`assign`.`employee_id` AND `event`.`id`=`task`.`event_id` AND `task`.`id`=`assign`.`task_id`"
    cm.execute(q)
    bc = cm.fetchall()
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})

@app.route('/task_report',methods=['GET'])
def task_report():
    cm,con = connection()
    mid=request.args.get('memid')
    fdate=request.args.get('sdate')
    tdate=request.args.get('edate')
    print("ooooooooooo",mid,fdate,tdate)
    r="SELECT `dept_id` FROM `employee` WHERE `employee`.`emp_id`='"+str(mid)+"'"
    cm.execute(r)
    ab=cm.fetchone()
    q = "SELECT `event`.`event_name`,`event`.`event_location`,`event`.`client_name`,`employee`.`f_name`,`employee`.`l_name` ,`employee`.`image`,`task`.`task`, `assign`.`estimation`,`assign`.`duration`,`assign`.`status` FROM `assign`,`employee`,`event`,`task` WHERE  `employee`.dept_id='"+str(ab[0])+"' AND `employee`.emp_id=`assign`.`employee_id` AND `event`.`id`=`task`.`event_id` AND `task`.`id`=`assign`.`task_id` and assign.task_date between '"+str(fdate)+"' and '"+str(tdate)+"'"
    cm.execute(q)
    bc = cm.fetchall()
    print("rrrrr",bc)
    row_header = [x[0]    for x in cm.description]
    json_data = []
    for result in bc:
        json_data.append(dict(zip(row_header, result)))
    return jsonify({"success":json_data})


if __name__ == '__main__':
    app.run(host='192.168.42.97',port=5000,debug=True)
