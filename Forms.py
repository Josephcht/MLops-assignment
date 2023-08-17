from wtforms import Form, StringField, SelectField, validators, IntegerField, PasswordField,MonthField, FloatField
class PredictionForm(Form):
    block = StringField('Block number:',[validators.DataRequired()])
    street_name = StringField('Street Name:', [validators.DataRequired()])
    town = StringField("Town:", [validators.DataRequired()])
    postal_code = IntegerField("Postal Code:",[validators.DataRequired(), validators.NumberRange(min=100000,max=999999,message='Invalid postal code. Please enter a valid postal code')] )
    month = MonthField("Year/Month that the house was last bought:", [validators.DataRequired()],format="%Y-%m")
    flat_type = SelectField('Flat Type:', [validators.DataRequired()], choices=[('', 'Select'),('1 ROOM', '1 ROOM'),('2 ROOM', '2 ROOM'), ('3 ROOM', '3 ROOM'), ('4 ROOM', '4 ROOM'),('5 ROOM', '5 ROOM'),('EXECUTIVE', 'EXECUTIVE'),('MULTI-GENERATION', 'MULTI-GENERATION')], default='')
    storey_range = SelectField('Storey Range:', [validators.DataRequired()], choices=[('01 TO 03', '01 TO 03'),('04 TO 06', '04 TO 06'),('07 TO 09', '07 TO 09'), ('10 TO 12', '10 TO 12'), ('13 TO 15', '13 TO 15'),('16 TO 18', '16 TO 18'),('19 TO 21', '19 TO 21'),('22 TO 24', '22 TO 24'),('25 TO 27', '25 TO 27'),('28 TO 30', '28 TO 30'),('31 TO 33', '31 TO 33'),('34 TO 36', '34 TO 36'),('37 TO 39', '37 TO 39'),('40 TO 42', '40 TO 42'),('43 TO 45', '43 TO 45'),('46 TO 48', '46 TO 48'),('49 TO 51', '49 TO 51')], default='01 TO 03')
    floor_area_sqm = FloatField('Floor Area Square Metre:',[validators.DataRequired()])
    flat_model = SelectField('Flat Model:', [validators.DataRequired()],
                            choices=[('', 'Select'), ('Model A', 'Model A'), ('Improved', 'Improved'), ('New Generation', 'New Generation'),
                                     ('Premium Apartment', 'Premium Apartment'), ('Simplified', 'Simplified'), ('Apartment', 'Apartment'),
                                     ('Maisonette', 'Maisonette'),('Standard', 'Standard'),('DBSS', 'DBSS'),('Model A2', 'Model A2'),('Type S1', 'Type S1'),
                                     ('Model A-Maisonette', 'Model A-Maisonette'),('Adjoined flat', 'Adjoined flat'),('Type S2', 'Type S2'),('Terrace', 'Terrace'),('Premium Apartment Loft', 'Premium Apartment Loft'),
                                     ('Multi Generation', 'Multi Generation'),('2-room', '2-room'),('Improved Maisonette', 'Improved-Maisonette'),('Premium Maisonette', 'Premium Maisonette'),('3Gen', '3Gen')], default='')
    lease_commence_date = IntegerField("Lease Commence Year:",[validators.DataRequired(), validators.NumberRange(min=1900,max=2024,message='Invalid Lease commence date. Please enter a valid year')] )
    cbd_dist = FloatField("Distance to the Central Business District from Home (m):",[validators.DataRequired()])
    min_dist_mrt = FloatField("Distance to nearest MRT (m):",[validators.DataRequired()])

class MyForm(Form):
    age = IntegerField('Age', [validators.DataRequired(), validators.NumberRange(min=0, max=100, message ='Invalid Age. Please enter a valid age.')])
    gender = SelectField('Gender', choices=[('F', 'F'), ('M', 'M')], validators=[validators.DataRequired()])
    chest_pain = SelectField('Chest Pain Type',  choices=[('ASY','ASY'),('NAP','NAP'),('ATA','ATA'),('TA','TA')], validators=[validators.DataRequired()])
    resting_BP = IntegerField('Resting Blood Pressure', [validators.DataRequired(), validators.NumberRange(min=0, max=300, message ='Invalid Resting Blood Pressure. Please enter a valid Blood Pressure rate.')])
    cholesterol = IntegerField('Cholesterol Level', [validators.DataRequired(), validators.NumberRange(min=0, max=1000, message ='Invalid Cholesterol Level. Please enter a valid Cholesterol Level.')])
    fasting_BS = SelectField('Fasting Blood Sugar (0: <100mg/dL, 1: 100-125mg/dL)',  choices=[('0', '0'), ('1', '1')], validators=[validators.DataRequired()])
    resting_ECG = SelectField('Resting ECG',  choices=[('Normal','Normal'),('LVH','LVH'),('ST','ST')], validators=[validators.DataRequired()])
    max_HR = IntegerField('Maximum Heart Rate', [validators.DataRequired(), validators.NumberRange(min=60, max=202, message ='Invalid Maximum Heart Rate. Please enter a valid Heart Rate.')])
    exercise_angina = SelectField('Exercise-induced angina',  choices=[('N','No'),('Y','Yes')], validators=[validators.DataRequired()])
    old_peak = FloatField('Old Peak', [validators.DataRequired(), validators.NumberRange(min=-5, max=10, message ='Invalid old peak. Please enter a valid old peak value.')])
    ST_slope = SelectField('Slope of peak exercise ST segment',  choices=[('Up','Up'),('Flat','Flat'), ('Down', 'Down')], validators=[validators.DataRequired()])
