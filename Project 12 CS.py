import pymysql as mc
from pymysql import Error

# ==================== DATABASE CONNECTION ====================
mydb=mc.connect(host="localhost",user="root",password="$elecT27")
mycursor=mydb.cursor()
rec1=[]
rec2=[]
rec3=[]
rec4=[]
mycursor.execute("CREATE DATABASE Project")
mycursor.execute("USE Project")
mycursor.execute("""
CREATE TABLE jee_math_syllabus (
    chapter_no INT PRIMARY KEY,
    chapter_name VARCHAR(100),
    days_required INT
);
""")
mycursor.execute("""
INSERT INTO jee_math_syllabus (chapter_no, chapter_name, days_required) VALUES
(1, 'Basic of Mathematics', NULL),
(2, 'Quadratic Equation', NULL),
(3, 'Complex Number', NULL),
(4, 'Sequences and Series', NULL),
(5, 'Permutation Combination', NULL),
(6, 'Binomial Theorem', NULL),
(7, 'Mathematical Reasoning',  NULL),
(8, 'Statistics', NULL),
(9, 'Matrices', NULL),
(10, 'Determinants', NULL),
(11, 'Probability', NULL),
(12, 'Sets and Relations', NULL),
(13, 'Functions', NULL),
(14, 'Limits', NULL),
(15, 'Continuity and Differentiability', NULL),
(16, 'Differentiation', NULL),
(17, 'Application of Derivatives', NULL),
(18, 'Indefinite Integration', NULL),
(19, 'Definite Integration', NULL),
(20, 'Area Under Curves', NULL),
(21, 'Differential Equations', NULL),
(22, 'Straight Lines', NULL),
(23, 'Circle', NULL),
(24, 'Parabola', NULL),
(25, 'Ellipse', NULL),
(26, 'Hyperbola', NULL),
(27, 'Trigonometric Ratios & Identities', NULL),
(28, 'Trigonometric Equations', NULL),
(29, 'Inverse Trigonometric Functions', NULL),
(30, 'Heights and Distances', NULL),
(31, 'Properties of Triangles', NULL),
(32, 'Vector Algebra', NULL),
(33, 'Three Dimensional Geometry', NULL);
""")
mydb.commit()
mycursor.execute("SELECT * FROM jee_math_syllabus")
for i in mycursor:
    rec1.append(i)
mycursor.execute("""
CREATE TABLE jee_physics_syllabus (
    chapter_no INT PRIMARY KEY,
    chapter_name VARCHAR(100),
    days_required INT
);
""")
mycursor.execute("""INSERT INTO jee_physics_syllabus (chapter_no, chapter_name, days_required) VALUES
(1, 'Mathematics in Physics', NULL),
(2, 'Units and Dimensions', NULL),
(3, 'Motion In One Dimension', NULL),
(4, 'Motion In Two Dimensions', NULL),
(5, 'Laws of Motion', NULL),
(6, 'Work Power Energy', NULL),
(7, 'Center of Mass Momentum and Collision', NULL),
(8, 'Rotational Motion', NULL),
(9, 'Gravitation', NULL),
(10, 'Mechanical Properties of Solids', NULL),
(11, 'Mechanical Properties of Fluids', NULL),
(12, 'Oscillations', NULL),
(13, 'Waves and Sound', NULL),
(14, 'Thermal Properties of Matter', NULL),
(15, 'Thermodynamics', NULL),
(16, 'Kinetic Theory of Gases', NULL),
(17, 'Electrostatics', NULL),
(18, 'Capacitance', NULL),
(19, 'Current Electricity', NULL),
(20, 'Magnetic Properties of Matter', NULL),
(21, 'Magnetic Effects of Current', NULL),
(22, 'Electromagnetic Induction', NULL),
(23, 'Alternating Current', NULL),
(24, 'Ray Optics', NULL),
(25, 'Wave Optics', NULL),
(26, 'Dual Nature of Matter', NULL),
(27, 'Atomic Physics', NULL),
(28, 'Nuclear Physics', NULL),
(29, 'Electromagnetic Waves', NULL),
(30, 'Semiconductors', NULL),
(31, 'Communication System', NULL),
(32, 'Experimental Physic', NULL);""")
mydb.commit()
mycursor.execute("SELECT * FROM jee_physics_syllabus")
for i in mycursor:
    rec2.append(i)
mycursor.execute("""
CREATE TABLE jee_chemistry_syllabus (
    chapter_no INT PRIMARY KEY,
    chapter_name VARCHAR(100),
    days_required INT
);
""")

mycursor.execute("""INSERT INTO jee_chemistry_syllabus (chapter_no, chapter_name, days_required) VALUES
(1, 'Some Basic Concepts of Chemistry', NULL),
(2, 'Structure of Atom', NULL),
(3, 'States of Matter', NULL),
(4, 'Thermodynamics (C)', NULL),
(5, 'Chemical Equilibrium', NULL),
(6, 'Ionic Equilibrium', NULL),
(7, 'Redox Reactions', NULL),
(8, 'Solid State', NULL),
(9, 'Solutions', NULL),
(10, 'Electrochemistry', NULL),
(11, 'Chemical Kinetics', NULL),
(12, 'Surface Chemistry', NULL),
(13, 'Classification of Elements and Periodicity in Properties', NULL),
(14, 'Chemical Bonding and Molecular Structure', NULL),
(15, 'Hydrogen', NULL),
(16, 's Block Elements', NULL),
(17, 'General Principles and Processes of Isolation of Metals', NULL),
(18, 'p Block Elements (Group 13 & 14)', NULL),
(19, 'p Block Elements (Group 15, 16, 17 & 18)', NULL),
(20, 'd and f Block Elements', NULL),
(21, 'Coordination Compounds', NULL),
(22, 'Practical Chemistry', NULL),
(23, 'General Organic Chemistry', NULL),
(24, 'Hydrocarbons', NULL),
(25, 'Environmental Chemistry', NULL),
(26, 'Haloalkanes and Haloarenes', NULL),
(27, 'Alcohols Phenols and Ethers', NULL),
(28, 'Aldehydes and Ketones', NULL),
(29, 'Carboxylic Acid Derivatives', NULL),
(30, 'Amines', NULL),
(31, 'Biomolecules', NULL),
(32, 'Polymers', NULL),
(33, 'Chemistry in Everyday Life', NULL);""")
mydb.commit()   
mycursor.execute("SELECT * FROM jee_chemistry_syllabus")
for i in mycursor:
    rec3.append(i)
mycursor.execute("""CREATE TABLE jee_study_plan (
    Week INT PRIMARY KEY,
    Maths VARCHAR(255),
    Physics VARCHAR(255),
    Chemistry VARCHAR(255),
    Weightage VARCHAR(50)
);""")
mycursor.execute("""INSERT INTO jee_study_plan (Week, Maths, Physics, Chemistry, Weightage) VALUES
(1, 'Basic of Mathematics', 'Mathematics in Physics', 'Some Basic Concepts of Chemistry', '2 + 2 + 2'),
(2, 'Quadratic Equation', 'Units and Dimensions', 'Structure of Atom', '3 + 2 + 3'),
(3, 'Complex Number', 'Motion In One Dimension', 'States of Matter', '2 + 2 + 2'),
(4, 'Sequences and Series', 'Motion In Two Dimensions', 'Thermodynamics (C)', '3 + 2 + 2'),
(5, 'Permutation Combination',' Laws of Motion', 'Chemical Equilibrium', '2 + 3 + 3'),
(6, 'Binomial Theorem', 'Work Power Energy', 'Ionic Equilibrium', '2 + 2 + 2'),
(7, 'Mathematical Reasoning', 'Center of Mass Momentum and Collision', 'Redox Reactions', '1 + 3 + 2'),
(8, 'Statistics', 'Rotational Motion', 'Solid State', '1 + 3 + 2'),
(9, 'Matrices', 'Gravitation', 'Solutions', '2 + 2 + 3'),
(10, 'Determinants', 'Mechanical Properties of Solids', 'Electrochemistry', '2 + 2 + 3'),
(11, 'Probability', 'Mechanical Properties of Fluids', 'Chemical Kinetics', '2 + 2 + 3'),
(12, 'Sets and Relations', 'Oscillations', 'Surface Chemistry', '2 + 3 + 2'),
(13, 'Functions', 'Waves and Sound', 'Classification of Elements and Periodicity in Properties', '2 + 2 + 2'),
(14, 'Limits', 'Thermal Properties of Matter', 'Chemical Bonding and Molecular Structure', '2 + 2 + 3'),
(15, 'Continuity and Differentiability', 'Thermodynamics', 'Hydrogen', '3 + 2 + 1'),
(16, 'Differentiation', 'Kinetic Theory of Gases', 's Block Elements', '2 + 2 + 2'),
(17, 'Application of Derivatives', 'Electrostatics', 'General Principles and Processes of Isolation of Metals', '3 + 3 + 2'),
(18, 'Indefinite Integration', 'Capacitance', 'p Block Elements (Group 13 & 14)', '2 + 2 + 2'),
(19, 'Definite Integration', 'Current Electricity', 'p Block Elements (Group 15, 16, 17 & 18)', '2 + 3 + 3'),
(20, 'Area Under Curves', 'Magnetic Properties of Matter', 'd and f Block Elements', '2 + 2 + 3'),
(21, 'Differential Equations', 'Magnetic Effects of Current', 'Coordination Compounds', '2 + 3 + 3'),
(22, 'Straight Lines', 'Electromagnetic Induction', 'Practical Chemistry', '2 + 3 + 2'),
(23, 'Circle', 'Alternating Current', 'General Organic Chemistry', '2 + 2 + 3'),
(24, 'Parabola', 'Ray Optics', 'Hydrocarbons', '2 + 3 + 3'),
(25, 'Ellipse', 'Wave Optics', 'Environmental Chemistry', '2 + 2 + 2'),
(26, 'Hyperbola', 'Dual Nature of Matter', 'Haloalkanes and Haloarenes', '2 + 2 + 2'),
(27, 'Trigonometric Ratios & Identities', 'Atomic Physics', 'Alcohols Phenols and Ethers', '2 + 2 + 2'),
(28, 'Trigonometric Equations', 'Nuclear Physics', 'Aldehydes and Ketones', '2 + 2 + 2'),
(29, 'Inverse Trigonometric Functions', 'Electromagnetic Waves', 'Carboxylic Acid Derivatives', '2 + 2 + 2'),
(30, 'Heights and Distances', 'Semiconductors', 'Amines', '1 + 2 + 2'),
(31, 'Properties of Triangles', 'Communication System', 'Biomolecules', '1 + 2 + 2'),
(32, 'Vector Algebra', 'Experimental Physics', 'Polymers', '2 + 2 + 2'),
(33, 'Three Dimensional Geometry', NULL, 'Chemistry in Everyday Life', '2 + NULL + 2');""")
mydb.commit()
mycursor.execute("SELECT * FROM jee_study_plan")
for i in mycursor:
    rec4.append(i)
tables = [
    "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m", "10m", "11m", "12m",
    "13m", "14m", "15m", "16m", "17m", "18m", "19m", "20m", "21m", "22m", "23m",
    "24m", "25m", "26m", "27m", "28m", "29m", "30m", "31m", "32m", "33m"
]

for table in tables:
    query = f"""
    CREATE TABLE IF NOT EXISTS {table} (
        sno INT PRIMARY KEY,
        topics VARCHAR(255),
        weightage VARCHAR(50)
    );
    """
    mycursor.execute(query)
mydb.commit()
physics_tables = [
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p", "12p",
    "13p", "14p", "15p", "16p", "17p", "18p", "19p", "20p", "21p", "22p", "23p",
    "24p", "25p", "26p", "27p", "28p", "29p", "30p", "31p", "32p"
]

for table in physics_tables:
    query = f"""
    CREATE TABLE IF NOT EXISTS {table} (
        sno INT PRIMARY KEY,
        topics VARCHAR(255),
        weightage VARCHAR(50)
    );
    """
    mycursor.execute(query)
mydb.commit()
chemistry_tables = [
    "1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "10c", "11c", "12c",
    "13c", "14c", "15c", "16c", "17c", "18c", "19c", "20c", "21c", "22c", "23c",
    "24c", "25c", "26c", "27c", "28c", "29c", "30c", "31c", "32c", "33c"
]

for table in chemistry_tables:
    query = f"""
    CREATE TABLE IF NOT EXISTS {table} (
        sno INT PRIMARY KEY,
        topics VARCHAR(255),
        weightage VARCHAR(50)
    );
    """
    mycursor.execute(query)

mydb.commit()
mycursor.execute("""
INSERT INTO 1m (sno, topics, weightage) VALUES
(1, 'Logarithm', NULL),
(2, 'Inequalities', NULL);""")
mydb.commit()
mycursor.execute("""
INSERT INTO 2m (sno, topics, weightage) VALUES
(1, 'Relation between Roots and Coefficients', 'High'),
(2, 'Graph and Sign of Quadratic', NULL),
(3, 'Range of Quadratic Function', NULL),
(4, 'Common Roots', NULL),
(5, 'Location of Roots', NULL),
(6, 'N degree equation', 'High');""")
mydb.commit()
mycursor.execute("""
INSERT INTO 3m (sno, topics, weightage) VALUES
(1, 'Power of iota', NULL),
(2, 'Algebra of complex numbers', NULL),
(3, 'Conjugate, modulus and argument', 'High'),
(4, 'Euler Form and De Moivres Theorem', 'High'),
(5, 'Cube Root of Unity', 'High'),
(6, 'Locus Based on Distance Formula', NULL),
(7, 'Geometry of Complex Number', 'High'),
(8, 'Rotation Theorem', NULL),
(9, 'nth roots of unity', NULL);""")
mydb.commit()
mycursor.execute("""
INSERT INTO 5m (sno, topics, weightage) VALUES
(1, 'Factorial', NULL),
(2, 'Permutation', 'High'),
(3, 'Combination', 'High'),
(4, 'Arrangement under Constraint', 'High'),
(5, 'Selection of one or more item', 'High'),
(6, 'Division and Distribution of Distinct Items', NULL),
(7, 'Division of Identical items', 'High'),
(8, 'Exponent of prime', NULL),
(9, 'Summation of Numbers', NULL),
(10, 'Geometric Permutation', NULL),
(11, 'Circular Permutation', NULL),
(12, 'Dearrangement', NULL);""")
mydb.commit()
mycursor.execute("""
INSERT INTO 4m (sno, topics, weightage) VALUES
(1, 'Arithmetic Progression', 'High'),
(2, 'Geometric Progression', 'High'),
(3, 'Mixed Question on AP and GP', 'High'),
(4, 'Means', NULL),
(5, 'Arithmetic Geometric Progression', 'High'),
(6, 'Summation of Series', 'High'),
(7, 'Inequalities', NULL);""")
mydb.commit()
mycursor.execute("""
INSERT INTO 6m (sno, topics, weightage) VALUES
(1, 'Terms of Binomial Expansion', 'High'),
(2, 'Remainder and Divisibility Problems', 'High'),
(3, 'Comparison between two numbers', NULL),
(4, 'Integral and Fractional Part of a Number', NULL),
(5, 'Properties of Binomial Coefficients', 'High'),
(6, 'Sum of Series', 'High'),
(7, 'Series involving Product of Coefficients', 'High'),
(8, 'Multinomial Theorem', NULL),
(9, 'Binomial Theorem for Negative Index', NULL);""")
mydb.commit()
mycursor.execute("""
INSERT INTO 27m (sno, topics, weightage) VALUES
(1, 'Basic Identities & T Ratios', NULL),
(2, 'Sum and Difference & Multiple angle Formula', 'High'),
(3, 'T-Ratios of Multiple & sub multiple angles', NULL),
(4, 'Transformation Formulas', NULL),
(5, 'Maximum and Minimum Values', NULL),
(6, 'Trigonometric Series', NULL);""")
mydb.commit()
mycursor.execute("""
INSERT INTO 28m (sno, topics, weightage) VALUES
(1, 'Solving Trigonometric Equation', 'High'),
(2, 'Solving Trigonometric Inequalities', NULL);""")
mydb.commit()
mycursor.execute("""
INSERT INTO 22m (sno, topics, weightage) VALUES
(1, 'Coordinate System', 'High'),
(2, 'Basic Forms of Straight Line', 'High'),
(3, 'Position of a point', NULL),
(4, 'Angle between Lines', NULL),
(5, 'Derived Forms of Line', NULL),
(6, 'Point and Line', 'High'),
(7, 'Concurrency & Family of Lines', NULL),
(8, 'Angle bisector', NULL),
(9, 'Locus', 'High'),
(10, 'Pair of Lines', NULL);""")
mydb.commit()

mycursor.execute("""
INSERT INTO 23m (sno, topics, weightage) VALUES
(1, 'General Equation of 2nd degree curve', NULL),
(2, 'Equation of Circle & its intercept', 'High'),
(3, 'Position of point', NULL),
(4, 'line and circle', 'High'),
(5, 'Tangent to circle', 'High'),
(6, 'Pair of Tangents', 'High'),
(7, 'Common Tangents', NULL),
(8, 'Chord of Contact', NULL),
(9, 'Chord with given Middle Point', NULL),
(10, 'Intersection of Circles', 'High'),
(11, 'Common Chord', NULL),
(12, 'Family of Circle', NULL),
(13, 'Locus', 'High');
""")
mydb.commit()

mycursor.execute("""
INSERT INTO 24m (sno, topics, weightage) VALUES
(1, 'standard equation of parabola', 'High'),
(2, 'Chord of parabola', 'High'),
(3, 'Line and parabola', NULL),
(4, 'Tangent to Parabola', 'High'),
(5, 'Pair of Tangents', NULL),
(6, 'Properties of Tangent', NULL),
(7, 'Common Tangent', 'High'),
(8, 'Normal to Parabola', NULL),
(9, 'Chord of Contact', NULL),
(10, 'Chord with given Middle Point', NULL),
(11, 'Locus', NULL);
""")
mydb.commit()

mycursor.execute("""
INSERT INTO 25m (sno, topics, weightage) VALUES
(1, 'Equation of Ellipse', 'High'),
(2, 'Position of point', NULL),
(3, 'Auxillary Circle', NULL),
(4, 'Line and ellipse', NULL),
(5, 'Chord of ellipse', NULL),
(6, 'Tangent to ellipse', 'High'),
(7, 'Pair of Tangents', NULL),
(8, 'Common Tangent', NULL),
(9, 'Normal to ellipse', NULL),
(10, 'Chord of Contact', NULL),
(11, 'Chord with given Middle Point', NULL),
(12, 'Locus', NULL),
(13, 'Reflection property', NULL);
""")
mydb.commit()

mycursor.execute("""
INSERT INTO 26m (sno, topics, weightage) VALUES
(1, 'Mixed Questions of Ellipse and Hyperbola', 'High'),
(2, 'Equation of hyperbola', 'High'),
(3, 'Tangent to hyperbola', 'High'),
(4, 'Common Tangent', NULL),
(5, 'Normal to hyperbola', 'High'),
(6, 'Chord with given Middle Point', NULL),
(7, 'Locus', NULL),
(8, 'Rectangular hyperbola', NULL);
""")
mydb.commit()
mycursor.execute("""
INSERT INTO 14m (sno, topics, weightage) VALUES
(1, 'Existance of Limit', NULL),
(2, 'Algebraic and Rational Limits', 'High'),
(3, 'Trigonometric and Inverse Trigonometric limits', 'High'),
(4, 'Exponential and logarithmic limits', NULL),
(5, 'Special Forms', 'High'),
(6, 'Miscellaneous', 'High');
""")
mydb.commit()


mycursor.execute("""
INSERT INTO 7m (sno, topics, weightage) VALUES
(1, 'Mathematical Reasoning', 'High');
""")
mydb.commit()


mycursor.execute("""
INSERT INTO 8m (sno, topics, weightage) VALUES
(1, 'Mean', NULL),
(2, 'Median', NULL),
(3, 'Measures of Dispersion', 'High'),
(4, 'Mean Square Deviation', NULL),
(5, 'Relation Between Variance and Mean Deviation', NULL);
""")
mydb.commit()


mycursor.execute("""
INSERT INTO 30m (sno, topics, weightage) VALUES
(1, 'Heights and Distances', 'High');
""")
mydb.commit()


mycursor.execute("""
INSERT INTO 31m (sno, topics, weightage) VALUES
(1, 'Sine Rule and its application', NULL),
(2, 'Cosine Rule and Projection Formula', NULL),
(3, 'Napiers Analogy, Area of Triangle & Half angle', NULL),
(4, 'Formulae', NULL),
(5, 'Circle Connected to Triangle', NULL);
""")


mycursor.execute("""
INSERT INTO 12m (sno, topics, weightage) VALUES
(1, 'Questions on Venn Diagram', 'High'),
(2, 'Questions on number of relations and sets', 'High'),
(3, 'Questions on Symmetric Transitive and Reflexive Properties', 'High');
""")


mycursor.execute("""
INSERT INTO 9m (sno, topics, weightage) VALUES
(1, 'Formation and Basic of Matrix', 'High'),
(2, 'Basic Algebra of Matrices', NULL),
(3, 'Symmetric & Skew Symmetric Matrices', NULL),
(4, 'Trace of a Matrix', NULL),
(5, 'Product of Matrices', 'High'),
(6, 'Adjoint and its Properties', 'High'),
(7, 'Inverse of a Matrix', 'High');
""")


mycursor.execute("""
INSERT INTO 10m(sno, topics, weightage) VALUES
(1, 'Expansion of Determinants', 'High'),
(2, 'System of Linear Equations', 'High'),
(3, 'Differentiation and Integration of Determinants', NULL),
(4, 'Summation of Determinants', NULL),
(5, 'Miscellaneous', NULL);
""")


mycursor.execute("""
INSERT INTO 29m (sno, topics, weightage) VALUES
(1, 'Principal Value and Basics', NULL),
(2, 'T inverse T property', NULL),
(3, 'Converting one Inverse T function to other Inverse T', NULL),
(4, 'Sum of complementary angles', NULL),
(5, 'Sum and difference of angles', 'High'),
(6, 'Multiple Angles', NULL),
(7, 'Infinite Series', NULL);
""")
mydb.commit()


mycursor.execute("""
INSERT INTO 13m(sno, topics, weightage) VALUES
(1, 'Domain', 'High'),
(2, 'Range', 'High'),
(3, 'Odd and Even Functions', NULL),
(4, 'Composite Function', 'High'),
(5, 'Periodicity', NULL),
(6, 'Types of Function (Mapping)', 'High'),
(7, 'Inverse of a Function', NULL),
(8, 'Functional Equation', 'High'),
(9, 'Number of Solutions', NULL),
(10, 'Definition of Function', NULL);
""")
mydb.commit()


mycursor.execute("""
INSERT INTO 15m (sno, topics, weightage) VALUES
(1, 'Continuity', 'High'),
(2, 'Differentiability', 'High');
""")


mycursor.execute("""
INSERT INTO 16m (sno, topics, weightage) VALUES
(1, 'Differentiation of composite functions', NULL),
(2, 'Differentiation of implicit functions', NULL),
(3, 'Parametric differentiation', NULL),
(4, 'Logarithmic differentiation', NULL),
(5, 'Derivative of f(x) wrt g(x)', NULL),
(6, 'Differentiation of Inverse Trigonometric Functions', NULL),
(7, 'Derivative of function and its inverse', NULL),
(8, 'Higher order derivatives', NULL),
(9, 'Functional Equation', NULL);
""")


mycursor.execute("""
INSERT INTO 17m (sno, topics, weightage) VALUES
(1, 'Maxima Minima', 'High'),
(2, 'Monotonicity', 'High'),
(3, 'Mean Value Theorem', 'High'),
(4, 'Rate Measure Error and Approximation', NULL),
(5, 'Tangent Normal', 'High');
""")


mycursor.execute("""
INSERT INTO 18m (sno, topics, weightage) VALUES
(1, 'Fundamental of Indefinite Integration', NULL),
(2, 'Integration by Substitution', 'High'),
(3, 'Integration by Parts', 'High'),
(4, 'Integration using Partial Fraction', NULL);
""")


mycursor.execute("""
INSERT INTO 19m (sno, topics, weightage) VALUES
(1, 'Basic Definite Integrals', NULL),
(2, 'Definite Integration by Substitution', 'High'),
(3, 'Definite Integration by Parts', 'High'),
(4, 'Properties of Definite Integration', 'High'),
(5, 'Properties of Periodic Functions', NULL),
(6, 'Leibnitz Rule of Differentiation', 'High'),
(7, 'Definite as Limit of Sum', NULL),
(8, 'Definite Integration by Reduction Formula', NULL),
(9, 'Properties Involving Inequalities', NULL),
(10, 'Miscellaneous', 'High');
""")


mycursor.execute("""
INSERT INTO 20m (sno, topics, weightage) VALUES
(1, 'Area of Curve along axis', 'High'),
(2, 'Area bounded by two curves', 'High'),
(3, 'Area bounded by Miscellaneous Curves', 'High');
""")


mycursor.execute("""
INSERT INTO 21m (sno, topics, weightage) VALUES
(1, 'Order and Degree', NULL),
(2, 'Formation of Differential Equation', NULL),
(3, 'Variable Separable Form', 'High'),
(4, 'Homogeneous DE', 'High'),
(5, 'Linear Differential Equation', 'High'),
(6, 'Exact Forms', 'High'),
(7, 'Applications of DE', 'High');
""")


mycursor.execute("""
INSERT INTO 32m (sno, topics, weightage) VALUES
(1, 'Algebra of Vectors', 'High'),
(2, 'Product of 2 vectors', 'High'),
(3, 'Scalar Triple Product', 'High'),
(4, 'Vector Triple Product', 'High');
""")


mycursor.execute("""
INSERT INTO 33m (sno, topics, weightage) VALUES
(1, 'Basics of point in 3 dimension', NULL),
(2, 'Direction Cosines and Direction Ratios', NULL),
(3, 'Line in Space', 'High'),
(4, 'Plane in Space', 'High'),
(5, 'Line and Plane', 'High');
""")


mycursor.execute("""
INSERT INTO 11m (sno, topics, weightage) VALUES
(1, 'Classical Definition of Probability', 'High'),
(2, 'Addition and Subtraction Theorems', NULL),
(3, 'Conditional Probability and Multiplication Theorem', 'High'),
(4, 'Independent Events', 'High'),
(5, 'Total Probability', NULL),
(6, "Baye's Theorem", 'High'),
(7, 'Bernoulli Trial and Binomial Distribution', 'High'),
(8, 'Random Variable and its Probability Distribution', 'High'),
(9, 'Geometric Probability', NULL);
""")
mydb.commit()

mycursor.execute("""
INSERT INTO 1c (sno, topics, weightage) VALUES
(1, 'Laws of chemical combination', NULL),
(2, 'Mole concept', 'High'),
(3, 'Quantitative measures in chemical equations', 'High'),
(4, 'Concentration terms', 'High'),
(5, 'Significant Figures', NULL);
""")
mydb.commit()

mycursor.execute("""
INSERT INTO 2c (sno, topics, weightage) VALUES
(1, 'Atomic Models', NULL),
(2, 'Atomic Mass and Atomic Size', NULL),
(3, "Bohr's model", 'High'),
(4, 'Hydrogen spectrum', 'High'),
(5, 'Dual Behaviour of Matter and Heisenberg Uncertainty Principle', 'High'),
(6, 'Quantum mechanical model', 'High'),
(7, 'Electronic configuration', 'High');
""")
mydb.commit()

mycursor.execute("""
INSERT INTO 13c (sno, topics, weightage) VALUES
(1, 'Earlier attempts of periodic classification', NULL),
(2, 'Modern periodic table', 'High'),
(3, 'Periodic properties', 'High');
""")

mycursor.execute("""
INSERT INTO 14c (sno, topics, weightage) VALUES
(1, 'Covalent and Co-ordinate Bonding', 'High'),
(2, 'Hybridisation and VSEPR Theory', 'High'),
(3, 'Back Bonding', NULL),
(4, 'Molecular Orbital Theory', 'High'),
(5, 'Characteristics of covalent compound', NULL),
(6, 'Ionic bond', NULL),
(7, 'Polarization', NULL),
(8, 'Properties of ionic compounds', NULL),
(9, 'Dipole moment', 'High'),
(10, 'Van Der Waals Forces, Hydrogen Bonding and Metallic Bonding', 'High');
""")

mycursor.execute("""
INSERT INTO 3c (sno, topics, weightage) VALUES
(1, 'Gas laws and Ideal Gas Equation', 'High'),
(2, 'Mixture of gases', NULL),
(3, 'Kinetic theory of gases', NULL),
(4, "Real Gases and Van der Waal's Equation", NULL),
(5, 'Critical phenomena and liquefaction', NULL),
(6, 'Liquid State', NULL);
""")

mycursor.execute("""
INSERT INTO 4c (sno, topics, weightage) VALUES
(1, 'System and surrounding', NULL),
(2, 'First Law and Basic Fundamentals of Thermodynamics', 'High'),
(3, 'Entropy and Second law of thermodynamics', 'High'),
(4, 'Third law of thermodynamics', 'High'),
(5, 'Carnot engine', NULL),
(6, 'Laws of Thermochemistry and Enthalpy Change', 'High');
""")

mycursor.execute("""
INSERT INTO 5c (sno, topics, weightage) VALUES
(1, "Le chatelier's principle", NULL),
(2, 'Law of Mass Action, Equilibrium Constant (Kc and Kp) and its Application', 'High');
""")

mycursor.execute("""
INSERT INTO 6c (sno, topics, weightage) VALUES
(1, 'Theories of Acids and Bases', 'High'),
(2, 'Ionic Product of Water', NULL),
(3, 'PH of solutions', 'High'),
(4, 'Salt Hydrolysis', NULL),
(5, 'Buffer solutions', NULL),
(6, 'Solubility', 'High'),
(7, 'Indicators', NULL);
""")

mycursor.execute("""
INSERT INTO 7c (sno, topics, weightage) VALUES
(1, 'Oxidation number', NULL),
(2, 'Oxidation and Reduction Reactions', NULL),
(3, 'Types of redox reactions', 'High'),
(4, 'Balancing of redox reactions', NULL),
(5, 'Equivalence concept', 'High'),
(6, 'Redox titration', 'High');
""")

mycursor.execute("""
INSERT INTO 15c (sno, topics, weightage) VALUES
(1, 'Preparation and Properties of Hydrogen', 'High'),
(2, 'Chemical properties of hydrogen', NULL),
(3, 'Hydrides', NULL),
(4, 'Preparation and Properties of Hydrogen Peroxide', NULL),
(5, 'Chemical properties of hydrogen peroxide', 'High'),
(6, 'Preparation and Properties of Water', 'High'),
(7, 'Chemical properties of heavy water', NULL);
""")

mycursor.execute("""
INSERT INTO 16c (sno, topics, weightage) VALUES
(1, 'Properties of S-block elements', 'High'),
(2, 'General Characteristics of Alkali Metals', 'High'),
(3, 'Compounds of Alkali Metals', NULL),
(4, 'Alkaline Earth Metals', 'High'),
(5, 'Compounds of Alkaline Earth Metals', 'High');
""")

mycursor.execute("""
INSERT INTO 18c (sno, topics, weightage) VALUES
(1, 'Boron and Its Compounds', 'High'),
(2, 'Aluminium and Its Compounds', NULL),
(3, 'Carbon and Its Compounds', 'High'),
(4, 'Silicon and Its Compounds', 'High'),
(5, 'Tin and Lead Containing Compounds', NULL);
""")

mycursor.execute("""
INSERT INTO 23c (sno, topics, weightage) VALUES
(1, 'IUPAC Nomenclature', 'High'),
(2, 'Classification of organic compounds', 'High'),
(3, 'Bond Cleavage', NULL),
(4, 'Reaction Intermediates', NULL),
(5, 'Electron displacement effects', 'High'),
(6, 'Conjugation and Aromaticity', 'High'),
(7, 'Attacking reagents', NULL),
(8, 'Isomerism of Organic Compounds', 'High'),
(9, 'Purification of Organic Compounds', 'High'),
(10, 'Qualitative analysis of organic compounds', 'High'),
(11, 'Quantitative analysis of organic compounds', 'High');
""")

mycursor.execute("""
INSERT INTO 24c (sno, topics, weightage) VALUES
(1, 'Properties and Preparation of Alkanes', NULL),
(2, 'Reactions of alkanes', 'High'),
(3, 'Properties and Preparation of Alkenes', 'High'),
(4, 'Reactions of alkenes', 'High'),
(5, 'Properties and Preparation of Alkynes', NULL),
(6, 'Reactions of alkynes', 'High'),
(7, 'Preparation and Reactions of cycloalkanes and cycloalkenes', NULL),
(8, 'Preparation and Reactions of Conjugate Dienes', NULL),
(9, 'Preparation and Properties of Benzene', NULL),
(10, 'Reactions of Benzene', NULL),
(11, 'Reactions of aromatic compounds', 'High');
""")

mycursor.execute("""
INSERT INTO 25c (sno, topics, weightage) VALUES
(1, 'Environmental Pollution and pollutants', NULL),
(2, 'Air Pollution', 'High'),
(3, 'Water Pollution', 'High'),
(4, 'Land Pollution', NULL),
(5, 'Control of environmental pollution', NULL);
""")

mycursor.execute("""
INSERT INTO 8c (sno, topics, weightage) VALUES
(1, 'Properties and Types of Solids', NULL),
(2, 'Crystal Structure of Solids', NULL),
(3, 'Cubic system', 'High'),
(4, 'Ionic structure', NULL),
(5, 'Stoichiometric defects', NULL),
(6, 'Non-stoichiometric defects', NULL),
(7, 'Electrical and Magnetic properties', NULL);
""")

mycursor.execute("""
INSERT INTO 9c (sno, topics, weightage) VALUES
(1, 'Solubility and Concentration of Solutions', 'High'),
(2, "Vapour pressure and raoult's law", 'High'),
(3, "Henry's law", NULL),
(4, 'Colligative Properties and Abnormal Molecular Masses', 'High');
""")

mycursor.execute("""
INSERT INTO 10c (sno, topics, weightage) VALUES
(1, 'Cells and Electrode Potential, Nernst Equation', 'High'),
(2, 'Types of half cells', NULL),
(3, 'Concentration cell', NULL),
(4, 'Commercial Cells and Batteries', NULL),
(5, 'Corrosion', NULL),
(6, 'Conductance and Conductivity', 'High');
""")

mycursor.execute("""
INSERT INTO 11c (sno, topics, weightage) VALUES
(1, 'Rate of reaction', 'High'),
(2, 'Rate law and rate constant', 'High'),
(3, 'Integrated rate laws', 'High'),
(4, 'Methods to determine order of reaction', 'High'),
(5, 'Parallel and Sequencial rate laws', NULL),
(6, 'Arrhenius theory', 'High'),
(7, 'Radioactivity', NULL);
""")

mycursor.execute("""
INSERT INTO 12c (sno, topics, weightage) VALUES
(1, 'Adsorption', 'High'),
(2, 'Adsorption isotherms', 'High'),
(3, 'Catalysis and Theories of Catalysis', NULL),
(4, 'Colloids', 'High'),
(5, 'Preparation and Purification of colloids', NULL),
(6, 'Properties of colloidal solution', 'High'),
(7, 'Emulsions and Gels', NULL),
(8, 'Nanostructures', NULL);
""")

mycursor.execute("""
INSERT INTO 17c (sno, topics, weightage) VALUES
(1, 'Minerals and ores', 'High'),
(2, 'Concentration of the Ore', 'High'),
(3, 'Reduction to Crude Metal', 'High'),
(4, 'Refining of Crude Metal', 'High'),
(5, 'Flux and Refractory materials', NULL),
(6, 'Extraction of Metals', 'High');
""")

mycursor.execute("""
INSERT INTO 19c (sno, topics, weightage) VALUES
(1, 'Nitrogen and Its Compounds', 'High'),
(2, 'Phosphorus and Its Compounds', 'High'),
(3, 'Oxygen and Its Compounds', NULL),
(4, 'Sulphur and Its Compounds', 'High'),
(5, 'Halogens and Its Compounds', 'High'),
(6, 'Noble Gases', NULL);
""")

mycursor.execute("""
INSERT INTO 20c (sno, topics, weightage) VALUES
(1, 'Properties of D-block elements', 'High'),
(2, 'Compounds of Transition Metals', 'High'),
(3, 'F-Block elements', 'High');
""")

mycursor.execute("""
INSERT INTO 21c (sno, topics, weightage) VALUES
(1, 'Terminology of coordination compounds', 'High'),
(2, 'Nomenclature of coordination compounds', NULL),
(3, 'Isomerism of coordination compounds', 'High'),
(4, "Werner's theory and Valence Bond Theory", 'High'),
(5, 'Crystal Field Theory', 'High'),
(6, 'Stability of complex ion', NULL),
(7, 'Carbonyl Compounds', NULL);
""")

mycursor.execute("""
INSERT INTO 26c (sno, topics, weightage) VALUES
(1, 'Preparation and Properties of Monohalides', 'High'),
(2, 'Preparation and Properties of Geminal and Vicinal Dihalides', NULL),
(3, 'Preparation and Properties of Aryl Halides', 'High'),
(4, 'Grignard Reagent', NULL);
""")

mycursor.execute("""
INSERT INTO 27c (sno, topics, weightage) VALUES
(1, 'Preparation and Properties of Alcohols', 'High'),
(2, 'Reactions of Alcohols', 'High'),
(3, 'Preparation of Phenols', NULL),
(4, 'Properties of Phenol', NULL),
(5, 'Reactions of Phenol', 'High'),
(6, 'Preparation of Ethers', NULL),
(7, 'Reactions of Ethers', 'High'),
(8, 'Preparation of Oxiranes', NULL),
(9, 'Reactions of Oxiranes', NULL),
(10, 'Dihydric alcohols', NULL),
(11, 'Preparation and Reactions of Glycol', NULL),
(12, 'Reactions of Carbonyl Compounds', NULL);
""")
mydb.commit()

mycursor.execute("""
INSERT INTO 28c (sno, topics, weightage) VALUES
(1, 'Method of preparation for both aldehydes and ketones', 'High'),
(2, 'Method of preparation for Aldehydes', 'High'),
(3, 'Method of preparation for Ketones', NULL),
(4, 'Chemical reactions for aldehydes and ketones', 'High'),
(5, 'Reactions for aldehydes', NULL),
(6, 'Reactions for ketones', NULL),
(7, 'Tests for aldehyde and ketones', 'High');
""")

mycursor.execute("""
INSERT INTO 29c (sno, topics, weightage) VALUES
(1, 'Preparation and Properties of Carboxylic Acids', 'High'),
(2, 'Reaction Involving Cleavage of –OH Group', NULL),
(3, 'Reactions Involving Acid Group', NULL),
(4, 'Abnormal Behaviour of Formic Acid', NULL),
(5, 'Preparation and Properties of Acid Derivatives', 'High'),
(6, 'Preparation and Properties of Esters', NULL);
""")

mycursor.execute("""
INSERT INTO 30c (sno, topics, weightage) VALUES
(1, 'Preparation and Properties of Amines', 'High'),
(2, 'Separation of mixture of amines', NULL),
(3, 'Nitrenes', NULL),
(4, 'Preparation and Properties of Amides', 'High'),
(5, 'Preparation and Properties of Cyanides', 'High'),
(6, 'Preparation and Properties of Isocyanides', NULL);
""")

mycursor.execute("""
INSERT INTO 31c (sno, topics, weightage) VALUES
(1, 'Carbohydrates', 'High'),
(2, 'Preparation and Reactions of Glucose', 'High'),
(3, 'Disaccharides and Polysaccharides', 'High'),
(4, 'Properties and Preparation of Amino Acids', 'High'),
(5, 'Proteins', 'High'),
(6, 'Nucleic Acids', 'High'),
(7, 'Vitamins', 'High'),
(8, 'Fats', NULL);
""")

mycursor.execute("""
INSERT INTO 32c (sno, topics, weightage) VALUES
(1, 'Classification of Polymers', 'High'),
(2, 'Preparation and Properties of Polymers', 'High');
""")

mycursor.execute("""
INSERT INTO 33c (sno, topics, weightage) VALUES
(1, "Drugs and It's Classification", 'High'),
(2, 'Cleansing Agents', NULL),
(3, 'Enzymes and Receptors', 'High'),
(4, 'Artificial Sweetning Agents and Food Preservatives', NULL);
""")

mycursor.execute("""
INSERT INTO 22c (sno, topics, weightage) VALUES
(1, 'Radicals', NULL),
(2, 'Preliminary Tests', 'High'),
(3, 'Identification of Acid Radicals', NULL),
(4, 'Identification of Basic Radicals', 'High');
""")
mydb.commit()
mycursor.execute("""
INSERT INTO 1p (sno, topics, weightage) VALUES
(1, 'Fundamentals of Vectors', NULL),
(2, 'Addition and Subtraction of Vectors', 'High'),
(3, 'Multiplication of Vectors', 'High'),
(4, "Lami's Theorem", NULL),
(5, 'Errors of Measurement', 'High');
""")

mycursor.execute("""
INSERT INTO 2p (sno, topics, weightage) VALUES
(1, 'Units', NULL),
(2, 'Dimensions', 'High');
""")

mycursor.execute("""
INSERT INTO 3p (sno, topics, weightage) VALUES
(1, 'Rest and Motion', 'High'),
(2, 'Uniform Motion', 'High'),
(3, 'Graphs of motion in one dimension', 'High'),
(4, 'Non-uniform Motion', 'High'),
(5, 'Relative Motion', NULL),
(6, 'Motion Under Gravity', 'High');
""")

mycursor.execute("""
INSERT INTO 4p (sno, topics, weightage) VALUES
(1, 'Relative motion', 'High'),
(2, 'Projectile motion', 'High'),
(3, 'Uniform Circular Motion', 'High');
""")

mycursor.execute("""
INSERT INTO 5p (sno, topics, weightage) VALUES
(1, "Newton's laws of motion", 'High'),
(2, 'Equilibrium of Forces', 'High'),
(3, 'Spring force', 'High'),
(4, 'Frictional force', 'High'),
(5, 'Non-uniform Circular Motion', 'High');
""")

mycursor.execute("""
INSERT INTO 6p (sno, topics, weightage) VALUES
(1, 'Work done', 'High'),
(2, 'Energy', 'High'),
(3, 'Power', 'High'),
(4, 'Circular motion', NULL);
""")

mycursor.execute("""
INSERT INTO 7p (sno, topics, weightage) VALUES
(1, 'momentum', 'High'),
(2, 'Centre of mass of discrete particles', NULL),
(3, 'Centre of mass of continuous mass distribution', 'High'),
(4, 'Motion of centre of mass', NULL),
(5, 'Impulse', NULL),
(6, 'Collisions', 'High'),
(7, 'Variable mass system', NULL);
""")

mycursor.execute("""
INSERT INTO 8p (sno, topics, weightage) VALUES
(1, 'Moment of inertia of rigid bodies', 'High'),
(2, 'Torque', 'High'),
(3, 'Rotational kinematics', 'High'),
(4, 'Angular momentum and Angular impulse', 'High'),
(5, 'Rolling without Slipping', 'High'),
(6, 'Combination of translation and rotation', NULL),
(7, 'Collisions in rotation', NULL);
""")

mycursor.execute("""
INSERT INTO 9p (sno, topics, weightage) VALUES
(1, "Newton's Law of Gravitation", 'High'),
(2, 'Gravitational field', NULL),
(3, 'Acceleration Due to Gravity', 'High'),
(4, 'Gravitational potential and Potential Energy', 'High'),
(5, 'Motion of satellite', 'High'),
(6, 'Kepler laws', NULL);
""")

mycursor.execute("""
INSERT INTO 10p (sno, topics, weightage) VALUES
(1, 'Elasticity', NULL),
(2, "Young's Modulus and Breaking Stress", 'High'),
(3, 'Bulk Modulus', 'High'),
(4, 'Shearing stress', NULL),
(5, 'Work Done in Stretching a Wire', NULL);
""")

mycursor.execute("""
INSERT INTO 11p (sno, topics, weightage) VALUES
(1, 'Density', NULL),
(2, 'Pressure and thrust', 'High'),
(3, "Pascal's Law", NULL),
(4, "Archmidies Principle", NULL),
(5, 'Hydrodynamics', 'High'),
(6, 'Efflux of liquid', NULL),
(7, 'Surface tension', 'High'),
(8, 'Viscosity', 'High');
""")

mycursor.execute("""
INSERT INTO 14p (sno, topics, weightage) VALUES
(1, 'Thermometry', NULL),
(2, 'Thermal Expansion', 'High'),
(3, 'Calorimetry', 'High'),
(4, 'Conduction', 'High'),
(5, 'Convection', NULL),
(6, 'Radiation', 'High');
""")

mycursor.execute("""
INSERT INTO 15p (sno, topics, weightage) VALUES
(1, 'Thermodynamic Systems', NULL),
(2, 'First Law of Thermodynamics', 'High'),
(3, 'Thermodynamic Processes', 'High'),
(4, 'Heat Engine, Refrigerator and Second Law of Thermodynamics', 'High');
""")

mycursor.execute("""
INSERT INTO 16p (sno, topics, weightage) VALUES
(1, 'Gas Laws', NULL),
(2, 'Speed of Gas', 'High'),
(3, 'Degree of Freedom and Specific Heat', 'High'),
(4, 'Pressure and Energy of gas', 'High');
""")

mycursor.execute("""
INSERT INTO 12p (sno, topics, weightage) VALUES
(1, 'Simple Harmonic Motion', 'High'),
(2, 'Energy of Simple Harmonic Motion', 'High'),
(3, 'Time Period and Frequency', 'High'),
(4, 'Applications of SHM', 'High'),
(5, "Superposition of S.H.M’s and Resonance", NULL),
(6, 'Angular oscillations', NULL);
""")

mycursor.execute("""
INSERT INTO 13p (sno, topics, weightage) VALUES
(1, 'Basics of Mechanical Waves', 'High'),
(2, 'Travelling Waves', 'High'),
(3, 'Interference and Superposition of Waves', NULL),
(4, 'Stationary waves', NULL),
(5, 'Vibration of String', 'High'),
(6, 'Organ Pipe (Vibration of Air Column)', 'High'),
(7, 'Beats', NULL),
(8, "Doppler's Effect", 'High'),
(9, 'Speed of Sound Waves', 'High'),
(10, 'Properties of Sound Waves', NULL);
""")

mycursor.execute("""
INSERT INTO 17p (sno, topics, weightage) VALUES
(1, "Electric Charge and Coulomb's law", 'High'),
(2, 'Electric Field and Electric Field Lines', 'High'),
(3, 'Electric Potential and Potential Energy', 'High'),
(4, 'Electric Dipole', 'High'),
(5, 'Electric Flux and Gauss Law', 'High');
""")

mycursor.execute("""
INSERT INTO 18p (sno, topics, weightage) VALUES
(1, 'Capacitance', 'High'),
(2, 'Grouping of capacitors', 'High'),
(3, 'Capacitors with Dielectric', 'High'),
(4, 'Force and Energy stored in capacitor', 'High'),
(5, 'Charging and Discarging of capacitors', NULL);
""")

mycursor.execute("""
INSERT INTO 19p (sno, topics, weightage) VALUES
(1, 'Electric Current and Drift of Electrons', 'High'),
(2, 'Resistance and Resistivity', 'High'),
(3, 'Color coding of resistors', NULL),
(4, 'Combination of Resistances', 'High'),
(5, 'Electric Cell or Battery', 'High'),
(6, "Kirchoffs Laws", 'High'),
(7, 'Electric Power and Heating Effect of Current', 'High'),
(8, 'Wheatstone Bridge', 'High'),
(9, 'Electric Instruments', 'High');
""")

mycursor.execute("""
INSERT INTO 20p (sno, topics, weightage) VALUES
(1, 'Magnetism and Properties of Magnet', 'High'),
(2, 'Earths magnetic field', 'High'),
(3, 'Magnetic Equipments', NULL),
(4, 'Magnetic Materials and their Properties', 'High');
""")

mycursor.execute("""
INSERT INTO 21p (sno, topics, weightage) VALUES
(1, "Biot-Savart’s Law and Ampere’s Circuital Law", NULL),
(2, 'Magnetic Field', 'High'),
(3, 'Motion of Charged Particle in Magnetic Field', 'High'),
(4, 'Force and Torque on Current Carrying Conductor', 'High'),
(5, 'Magnetic Moment', 'High'),
(6, 'Magnetic Dipole', NULL);
""")

mydb.commit()
# ==================== ROBUST COLUMN CHECK & ADD ====================
def ensure_column_exists(table_name, column_name="status", data_type="VARCHAR(20) DEFAULT 'Pending'"):
    """Adds a column only if it doesn't already exist in the specified table."""
    try:
        # 1. Check if the column exists
        mycursor.execute(f"""
            SELECT COUNT(*)
            FROM information_schema.COLUMNS
            WHERE TABLE_SCHEMA = 'Project'
            AND TABLE_NAME = '{table_name}'
            AND COLUMN_NAME = '{column_name}'
        """)
        
        if mycursor.fetchone()[0] == 0:
            # 2. If the column does not exist, add it
            mycursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}")
            mydb.commit()
            
    except Error as e:
        # Catch errors if the database or table doesn't exist (though unlikely here)
        print(f"❌ Error during column check for {table_name}: {e}")

# Fix for the SQL syntax error: Run column checks on the main syllabus tables
ensure_column_exists("jee_math_syllabus")
ensure_column_exists("jee_physics_syllabus")
ensure_column_exists("jee_chemistry_syllabus")

# ==================== HELPER FUNCTIONS ====================

def get_syllabus_table(subject_suffix):
    if subject_suffix == "m":
        return "jee_math_syllabus"
    elif subject_suffix == "p":
        return "jee_physics_syllabus"
    elif subject_suffix == "c":
        return "jee_chemistry_syllabus"

def subject_full_name(suffix):
    return {"m": "Mathematics", "p": "Physics", "c": "Chemistry"}.get(suffix, "Unknown")

# ==================== CHAPTER TOPIC DISPLAY ====================

def show_chapter_topics(subject_suffix):
    syllabus_table = get_syllabus_table(subject_suffix)
    choice = input("Do you want to enter Chapter Number (n) or Name (name)? ").strip().lower()

    chap_num = None
    if choice == "n":
        try:
            # --- Exception Handling for Chapter Number Input ---
            chap_num = int(input("Enter the chapter number: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            return
    else:
        chap_name = input("Enter the chapter name or part of it: ").strip()
        mycursor.execute(f"SELECT chapter_no, chapter_name FROM {syllabus_table} WHERE chapter_name LIKE %s", (f"%{chap_name}%",))
        results = mycursor.fetchall()
        
        if not results:
            print("❌ Chapter not found.")
            return
            
        if len(results) > 1:
            print("\nMultiple matches found:")
            for r in results:
                print(f"{r[0]} - {r[1]}")
            try:
                # --- Exception Handling for Selecting Chapter Number ---
                chap_num = int(input("\nEnter the correct chapter number from above: "))
            except ValueError:
                print("❌ Invalid input. Please enter a number from the list.")
                return
        else:
            chap_num = results[0][0]
    
    if chap_num is None:
        return

    table_name = f"{chap_num}{subject_suffix}"

    # --- Check table existence ---
    mycursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    if not mycursor.fetchone():
        print(f"❌ Topic table '{table_name}' doesn't exist for this chapter.")
        return

    # --- Ensure 'status' column exists in topic table ---
    ensure_column_exists(table_name, data_type="VARCHAR(20) DEFAULT 'Pending'")
    
    # --- Fetch topics ---
    mycursor.execute(f"SELECT * FROM {table_name}")
    rows = mycursor.fetchall()
    if rows:
        print(f"\n📘 Topics for Chapter {chap_num} ({table_name}) - {subject_full_name(subject_suffix)}")
        print("---------------------------------------------------")
        for row in rows:
            sno = row[0]
            topic = row[1]
            weight = row[2] if len(row) > 2 and row[2] else "No weightage"
            status = row[3] if len(row) > 3 and row[3] else "Pending"
            
            status_symbol = "✅" if status == "Completed" else "⏳"
            
            print(f"{sno}. {status_symbol} {topic} — {weight}")
        print("---------------------------------------------------")
        print(f"✅ Total topics: {len(rows)}")
    else:
        print("❌ No topics found for this chapter.")

# ==================== PROGRESS TRACKER ====================
# (No changes needed here as there is no user input)

def syllabus_progress(subject_suffix):
    syllabus_table = get_syllabus_table(subject_suffix)
    mycursor.execute(f"SELECT COUNT(*) FROM {syllabus_table}")
    total_chapters = mycursor.fetchone()[0]
    mycursor.execute(f"SELECT COUNT(*) FROM {syllabus_table} WHERE status='Completed'")
    completed_chapters = mycursor.fetchone()[0]

    percent = (completed_chapters / total_chapters) * 100 if total_chapters else 0
    
    # --- Calculate Overall Topic Progress ---
    total_topics = 0
    completed_topics = 0
    
    mycursor.execute(f"SELECT chapter_no FROM {syllabus_table}")
    chapter_numbers = [c[0] for c in mycursor.fetchall()]
    
    for chap_num in chapter_numbers:
        topic_table = f"{chap_num}{subject_suffix}"
        
        # Check table existence to avoid crashing on non-existent topic tables
        mycursor.execute(f"SHOW TABLES LIKE '{topic_table}'")
        if not mycursor.fetchone():
            continue
            
        ensure_column_exists(topic_table)

        mycursor.execute(f"SELECT COUNT(*) FROM {topic_table}")
        count = mycursor.fetchone()[0]
        total_topics += count
        
        mycursor.execute(f"SELECT COUNT(*) FROM {topic_table} WHERE status='Completed'")
        count_completed = mycursor.fetchone()[0]
        completed_topics += count_completed

    topic_percent = (completed_topics / total_topics) * 100 if total_topics else 0

    print(f"\n📊 Progress Report - {subject_full_name(subject_suffix)}")
    print("--- Chapter Progress ---")
    print(f"Total Chapters: {total_chapters}")
    print(f"Completed Chapters: {completed_chapters}")
    print(f"Pending Chapters: {total_chapters - completed_chapters}")
    print(f"Chapter Progress: {percent:.2f}% ✅")
    print("--- Topic Progress (Overall) ---")
    print(f"Total Topics: {total_topics}")
    print(f"Completed Topics: {completed_topics}")
    print(f"Topic Progress: {topic_percent:.2f}% (Average) ✅")


# ==================== MARK TOPIC AS COMPLETED ====================

def mark_topic_completed(subject_suffix):
    try:
        # --- Exception Handling for Topic Numbers ---
        chap_num = int(input("Enter the chapter number: "))
        topic_sno = int(input("Enter the topic S.No. to mark as Completed: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number for both Chapter and Topic S.No.")
        return

    topic_table = f"{chap_num}{subject_suffix}"
    
    mycursor.execute(f"SHOW TABLES LIKE '{topic_table}'")
    if not mycursor.fetchone():
        print(f"❌ Topic table '{topic_table}' doesn't exist for this chapter. Cannot mark topic.")
        return

    ensure_column_exists(topic_table)

    # Check if topic exists
    mycursor.execute(f"SELECT topic_name FROM {topic_table} WHERE S_No = %s", (topic_sno,))
    result = mycursor.fetchone()
    
    if not result:
        print(f"❌ Topic S.No. {topic_sno} not found in Chapter {chap_num}.")
        return

    topic_name = result[0]
    
    # Update topic status
    mycursor.execute(f"UPDATE {topic_table} SET status='Completed' WHERE S_No=%s", (topic_sno,))
    
    # Check if all topics in the chapter are now complete
    mycursor.execute(f"SELECT COUNT(*) FROM {topic_table} WHERE status!='Completed'")
    pending_topics = mycursor.fetchone()[0]

    syllabus_table = get_syllabus_table(subject_suffix)
    if pending_topics == 0:
        # Automatically mark the chapter as 'Completed'
        mycursor.execute(f"UPDATE {syllabus_table} SET status='Completed' WHERE chapter_no=%s", (chap_num,))
        mydb.commit()
        print(f"✅ Chapter {chap_num} ('{topic_table}') automatically marked as Completed! 🥳")
    else:
        # Ensure chapter status is 'Pending' if not all topics are done
        mycursor.execute(f"UPDATE {syllabus_table} SET status='Pending' WHERE chapter_no=%s AND status='Completed'", (chap_num,))
        
    mydb.commit()
    print(f"✅ Topic '{topic_name}' marked as Completed!")


# ==================== MARK CHAPTER AS COMPLETED ====================

def mark_chapter_completed(subject_suffix):
    syllabus_table = get_syllabus_table(subject_suffix)
    try:
        # --- Exception Handling for Chapter Number Input ---
        chap_num = int(input("Enter the chapter number to mark as Completed: "))
    except ValueError:
        print("❌ Invalid input. Please enter a chapter number.")
        return
        
    mycursor.execute(f"SELECT chapter_name FROM {syllabus_table} WHERE chapter_no = %s", (chap_num,))
    result = mycursor.fetchone()
    if not result:
        print("❌ Chapter not found.")
        return
    
    chapter_name = result[0]
    topic_table = f"{chap_num}{subject_suffix}"
    
    # When a chapter is manually marked complete, mark all its topics complete
    mycursor.execute(f"SHOW TABLES LIKE '{topic_table}'")
    if mycursor.fetchone():
        ensure_column_exists(topic_table)
        mycursor.execute(f"UPDATE {topic_table} SET status='Completed'")
    
    # Update chapter status
    mycursor.execute(f"UPDATE {syllabus_table} SET status='Completed' WHERE chapter_no=%s", (chap_num,))
    mydb.commit()
    
    print(f"✅ Chapter '{chapter_name}' marked as Completed (and all its topics)! 🥳")

# ==================== MENU ====================

def subject_menu(subject_suffix):
    syllabus_table = get_syllabus_table(subject_suffix)
    mycursor.execute(f"SELECT chapter_no, chapter_name, status FROM {syllabus_table}")
    chapters = mycursor.fetchall()

    print(f"\n📚 {subject_full_name(subject_suffix)} - Syllabus")
    for c in chapters:
        status_symbol = "✅" if c[2] == "Completed" else "⏳"
        print(f"{c[0]}. {c[1]} — {status_symbol} {c[2]}")
    print("---------------------------------------------------")

    while True:
        print("\nOptions:")
        print("1 - View Chapter Topics")
        print("2 - Mark Chapter as Completed")
        print("3 - Mark Topic as Completed")
        print("4 - View Progress Tracker")
        print("5 - Back to Main Menu")
        opt = input("Enter your choice: ").strip()

        # --- Exception Handling for Menu Choice ---
        if opt == "1":
            show_chapter_topics(subject_suffix)
        elif opt == "2":
            mark_chapter_completed(subject_suffix)
        elif opt == "3":
            mark_topic_completed(subject_suffix)
        elif opt == "4":
            syllabus_progress(subject_suffix)
        elif opt == "5":
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 5.")

# ==================== MAIN ====================

def main():
    print("✨ Welcome to SPARKS - JEE Study Planner ✨\n")
    
    while True:
        print("\nMain Menu:")
        print("1 - Mathematics")
        print("2 - Physics")
        print("3 - Chemistry")
        print("4 - Exit")
        choice = input("Enter your choice: ").strip()

        # --- Exception Handling for Main Menu Choice ---
        if choice == "1":
            subject_menu("m")
        elif choice == "2":
            subject_menu("p")
        elif choice == "3":
            subject_menu("c")
        elif choice == "4":
            print("👋 Exiting SPARKS. All the best for your JEE!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 4.")

    if mydb.is_connected():
        mydb.commit()
        mycursor.close()
        mydb.close()

# ==================== PROGRAM START ====================
if __name__ == "__main__":
    main()