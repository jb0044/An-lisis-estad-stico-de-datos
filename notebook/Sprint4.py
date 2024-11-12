#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Jorge!
# 
# Mi nombre es Ezequiel Ferrario, soy code reviewer en Tripleten y tengo el agrado de revisar el proyecto que entregaste.
# 
# Para simular la dinámica de un ambiente de trabajo, si veo algún error, en primer instancia solo los señalaré, dándote la oportunidad de encontrarlos y corregirlos por tu cuenta. En un trabajo real, el líder de tu equipo hará una dinámica similar. En caso de que no puedas resolver la tarea, te daré una información más precisa en la próxima revisión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres**.
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta. Se aceptan uno o dos comentarios de este tipo en el borrador, pero si hay más, deberá hacer las correcciones. Es como una tarea de prueba al solicitar un trabajo: muchos pequeños errores pueden hacer que un candidato sea rechazado.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# 
# Hola, muchas gracias por tus comentarios y la revisión. Referente a este comentarios que indicaste:
# 
# Comentario del revisor
# 
# Cuidado, el paso de gb a mb deberiamos hacerlo luego de hacer las tablas pivots (o groupby) ya que de lo contrario podriamos estar sobreeestimando el consumo de los mismos. **Me comentó mi tutor Rodo Núñez que esta parte de conversión de gb si está bien ubicada en esta zona. Hola revisor!!!, ya traté de corregir todo lo que me has pedido, solo hay un detalle de los lineplot, pero ya hablé con compañeros sobre el proyecto y me comentan que ya así está bien, ya urge pasar al proyecto del sprint 5, cada vez que te lo mando, me pones una nueva corrección que ni estaba antes.
# 
# </div>
# 
# ¡Empecemos!

# # ¿Cuál es la mejor tarifa?
# 
# Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
# Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

# ## Inicialización

# In[1]:


import pandas as pd 
import seaborn as sns 
import numpy as np 
from math import factorial
from scipy import stats as st
import math as mt
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import plotly.express as px# Cargar todas las librerías


# ## Cargar datos

# In[2]:


megacalls_df = pd.read_csv('/datasets/megaline_calls.csv') # Carga los archivos de datos en diferentes DataFrames

internet_df = pd.read_csv('/datasets/megaline_internet.csv')

msn_df = pd.read_csv('/datasets/megaline_messages.csv')

plans_df = pd.read_csv('/datasets/megaline_plans.csv')

users_df = pd.read_csv('/datasets/megaline_users.csv')


# ## Preparar los datos

# ## Tarifas

# In[3]:


plans_df.info() # Imprime la información general/resumida sobre el DataFrame de las tarifas



# In[4]:


(plans_df.describe())

(plans_df.head(5))# Imprime una muestra de los datos para las tarifas



# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Al leer el dataframe de tarifas, al parecer no se observan datos ausentes, tenemos 5 columnas con tipo de datos de enteros, 2 tipo float y una tipo object. 

# ## Corregir datos

# Al revisar valores duplicados y ausentes, no existen.

# In[5]:


(plans_df.duplicated().sum()) #Revisar valores duplicados


# In[6]:


plans_df.isna().sum() #Encuentra valores ausentes en la tabla de plans


# In[7]:


#Convertir a gb
plans_df['gb_per_month_included'] = plans_df['mb_per_month_included']/1024 
    
    

   


# ## Enriquecer los datos

# In[8]:


#Incluir nueva column'gb_per_month_included'. quitando la columna de 'mb_per_month_included'.   
plans_df.drop(columns='mb_per_month_included', inplace=True)
plans_df.info()


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Excelente.</div>

# ## Usuarios/as

# In[9]:


users_df.info()# Imprime la información general/resumida sobre el DataFrame de usuarios


# In[10]:


users_df.describe()

users_df.head(5)# Imprime una muestra de datos para usuarios


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[11]:


users_df.isna().sum() #Encuentra valores ausentes en la tabla de users


# In[12]:


users_df.duplicated().sum() #Encuentra valores duplicados en la tabla de users


# Al leer el dataframe de users, la columna 'churn_date' cuenta con datos ausentes debido a que se refiere a la fecha en la que el usuario canceló su plan, y sólo algunos usuarios lo han cancelado. No hay valores duplicados. Tenemos 6 columnas con tipo de datos de objetos y 2 con tipo entero. 

# ### Corregir los datos
Se identificó que es recomendable reemplazar los datos nulos de la columna 'churn_date' por 'active_user' para hacer diferencia de los exclientes, y los datos de fechas se cambiaron a datetime como en las columnas; 'reg_date', 'churn_date'. Además mediante el metódo dt.month se extraera el número del mes de la columna 'reg_date', para uso de calculos posteriores. 
# In[13]:


users_df['churn_date'] = pd.to_datetime(users_df['churn_date']) #Transformamos las columnas a tipo de datetime
print("Después: ", users_df['churn_date'].dtypes)
users_df['reg_date'] = pd.to_datetime(users_df['reg_date'])
print("Después: ", users_df['reg_date'].dtypes)



# ### Enriquecer los datos

# In[14]:


users_df['churn_date'] = users_df['churn_date'].fillna('active_user')
users_df.isnull().sum()


# ## Llamadas

# In[15]:


megacalls_df.info()# Imprime la información general/resumida sobre el DataFrame de las llamadas


# In[16]:


megacalls_df.describe()

megacalls_df.head(5)# Imprime una muestra de datos para las llamadas


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Los datos de fechas se cambiaron a datetime en la columna 'call_date'. Además mediante el metódo dt.month se extraera el número del mes de la columna 'call_date', para uso de calculos posteriores. 

# ### Corregir los datos

# In[17]:


megacalls_df['call_date'] = pd.to_datetime(megacalls_df['call_date']) #Transformamos la columna a tipo de datetime
print("Después: ", megacalls_df['call_date'].dtypes)


# In[18]:


#Redondear las duración de llamadas al siguiente numero entero
megacalls_df['duration']=np.ceil(megacalls_df['duration'])


# In[19]:


#Cambia nombre de la columna
megacalls_df.rename(columns={"id": "id_call"}, inplace=True)
megacalls_df.head(4)


# In[20]:


megacalls_df['id_call'] = megacalls_df['id_call'].astype(int) #Cambiamos el tipo de datos a entero
megacalls_df.info()


# ### Enriquecer los datos

# In[21]:


megacalls_df['call_date'] = megacalls_df['call_date'].dt.month #Extraemos el número de mes de dicha columna
megacalls_df.head(5)



# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[22]:


megacalls_df.rename(columns={"call_date": "month"}, inplace=True) #Renombrar columna
megacalls_df.sample(3)


# ## Mensajes

# In[23]:


msn_df.info()# Imprime la información general/resumida sobre el DataFrame de los mensajes


# In[24]:


msn_df.describe()

msn_df.sample(5)# Imprime una muestra de datos para los mensajes


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Al leer el dataframe de mensajes, la columna 'message_date' de tipo objeto, tiene que ser cambiada a tipo fecha. Tenemos 2 columnas con tipo de datos de objetos y 2 con tipo entero. No hay datos nulos. Hay elementos duplicados pero es debido a que el mismo usuario mando multiples mensajes durantes distintos tiempos.

# ### Corregir los datos

# In[25]:


msn_df['message_date'] = pd.to_datetime(msn_df['message_date']) #Transformamos la columna a tipo de datetime
print("Después: ", msn_df['message_date'].dtypes)


# In[26]:


msn_df.rename(columns={"id": "id_message"}, inplace=True) #Renombrar columna
msn_df.head(2)


# In[27]:


msn_df['id_message'] = msn_df['id_message'].astype(int) #Cambiar tipos de datos a entero
msn_df.info()


# ### Enriquecer los datos

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda que lo que esta entre corchete es una mera guia para el alumno. Este al ser un proyecto simulando un espacio profesional, deberias eliminar los mismos.
# 
# Esta correccion aplica a cualquier parte donde se encuentre este tipo de guias ya que es un requisito de **forma** obligatorio para aprobar el proyecto (es decir, que no quede ninguna guia/corchete).</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[28]:


msn_df['message_date'] = msn_df['message_date'].dt.month #Extraemos el número de mes de dicha columna
msn_df.head(5)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[29]:


msn_df.rename(columns={"message_date": "month"}, inplace=True) #Renombrar columna
msn_df.sample(5)


# ## Internet

# In[30]:


internet_df.info()

internet_df.describe()# Imprime la información general/resumida sobre el DataFrame de internet


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda utilizar el metodo describe() para una exploracion rapida inicial de aquellas variables numericas. Siempre es necesario realizarlo ya que de forma rapida tenemos un panorama muy bueno de que nos espera e incluso encontraremos inconsistencias si existiencen.
# Describi al respecto lo que ves. </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[31]:


internet_df.sample(n=4) # Imprime una muestra de datos para el tráfico de internet


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# Al leer el dataframe de Internet, la columna 'session_date' de tipo objeto, tiene que ser cambiada a tipo datetime. Tenemos 2 columnas con tipo de datos de objetos, una de float y una con entero. No hay datos nulos. Hay elementos duplicados pero es debido a que el mismo usuario usó los datos durantes distintos tiempos. Además mediante el metódo dt.month se extraerá el número del mes de la columna 'session_date', para uso de calculos posteriores. 

# ### Corregir los datos

# In[32]:


internet_df['session_date'] = pd.to_datetime(internet_df['session_date']) #Transformamos la columna a tipo de datetime
print("Después: ", internet_df['session_date'].dtypes)


# In[33]:


internet_df.rename(columns={"id": "id_internet"}, inplace=True) #Renombrar columna
internet_df.sample(n=5)


# In[34]:


internet_df['id_internet'] = internet_df['id_internet'].astype(int) #Transformar a tipo de dato entero
internet_df.info()


# ### Enriquecer los datos

# In[35]:


internet_df['session_date'] = internet_df['session_date'].dt.month #Extraemos el número de mes de dicha columna
internet_df.head(5)


# In[36]:


internet_df.rename(columns={"session_date": "month"}, inplace=True) #Renombrar columna
internet_df.info()


# In[37]:


internet_df['gb_used']=internet_df['mb_used']/1024  #Se cambian los datos de mbs a gbs para su analisís posterior
internet_df['gb_used']


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Cuidado, el paso de gb a mb deberiamos hacerlo luego de hacer las tablas pivots (o groupby) ya que de lo contrario podriamos estar sobreeestimando el consumo de los mismos. **Me comentó mi tutor Rodo Núñez que esta parte de conversión de gb si está bien ubicada en esta zona. 
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Jorge, en este caso te pido disculpas ya que en este caso esta perfecto lo que realizaste.
# 
# Se me paso por arriba el comentario y pense que realizabas el ceiling haciendo que se sobreestime el consumo, pero no es asi. Muy bien.</div>

# In[38]:


internet_df.info()


# ## Estudiar las condiciones de las tarifas

# In[39]:


# Imprime las condiciones de la tarifa y asegúrate de que te quedan claras
plans_df


# In[40]:


# Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.
monthly_calls = megacalls_df.groupby(['user_id','month'])['id_call'].count().reset_index(name='calls_made')

monthly_calls.head(20)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[41]:


# Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.
monthly_min_calls = megacalls_df.groupby(['user_id','month'])['duration'].sum().reset_index(name='duration_calls')

monthly_min_calls.head(20)


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[42]:


# Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.
monthly_sms = msn_df.groupby(['user_id','month'])['id_message'].count().reset_index(name='messages_used')

monthly_sms.head(20)



# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[43]:


monthly_mbs = internet_df.groupby(['user_id','month'])['mb_used'].sum().reset_index()# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.
monthly_mbs


# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta bien. Pero en este caso remplaza el print() y utiliza el metodo sin nada (llamalo solo) o con el metodo display(). Esto hara que sea mas legible y estetico.</div>

# In[44]:


monthly_gbs = internet_df.groupby(['user_id','month'])['gb_used'].sum().reset_index()
monthly_gbs


# In[45]:


# Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month
fusion_data = (monthly_calls
                .merge(monthly_min_calls, 
                       on=['user_id','month'],
                       how='outer')
                .merge(monthly_sms, 
                       on=['user_id','month'],
                       how='outer')
                .merge(monthly_gbs, on=['user_id','month'],
                       how='outer')) 
fusion_data


# In[46]:


fusion_data_plus_users = pd.merge(fusion_data,users_df[['user_id','city','plan']],on='user_id')
fusion_data_plus_users.info()


# In[47]:


fusion_final=fusion_data_plus_users.merge(plans_df,left_on='plan',right_on='plan_name').drop(columns='plan_name')
fusion_final.info()


# In[48]:


fusion_final.isna().sum()



# In[49]:


fusion_final['calls_made'].fillna(0,inplace=True)
fusion_final['duration_calls'].fillna(0,inplace=True)
fusion_final['messages_used'].fillna(0,inplace=True)
fusion_final['gb_used'].fillna(0,inplace=True)

fusion_final.info()


# In[50]:


fusion_final['gb_used']=np.ceil(fusion_final['gb_used'])


# In[51]:


extra_calls = fusion_final['duration_calls'] - fusion_final['minutes_included']
fusion_final['extra_calls']=np.where(extra_calls<0,0,extra_calls) * fusion_final['usd_per_minute']         
extra_sms = fusion_final['messages_used'] - fusion_final['messages_included']
fusion_final['extra_sms']=np.where(extra_sms<0,0,extra_sms) * fusion_final['usd_per_message'] 
extra_gbs = fusion_final['gb_used'] - fusion_final['gb_per_month_included']
fusion_final['extra_gbs']=np.where(extra_gbs<0,0,extra_gbs) * fusion_final['usd_per_gb'] 

fusion_final['final_income']=fusion_final['extra_calls']+fusion_final['extra_sms']+fusion_final['extra_gbs']+fusion_final['usd_monthly_pay']        


# In[52]:


fusion_final.sort_values(by='user_id')
fusion_final.info()


# In[53]:


plans_df # Añade la información de la tarifa


# Se hizo una tabla para fusionar los datos de llamadas, mensajes e internet, con el objetivo de contar con toda la información en un mismo df, para facilitar los diferentes calculos necesarios para su proceso analítico.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Describi y conclui al respecto de lo realizado en en esta seccion. Esta parte es muy importante debido que es aqui donde tambien esta nuestro valor, ya que el cliente podra no entender el código pero si el análisis o la descripcion.</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# ## Estudia el comportamiento de usuario

# ### Llamadas

# In[54]:


# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.
mean_calls = fusion_final.groupby(['plan','month'])['duration_calls'].mean().reset_index()


mean_duration_calls_surf = mean_calls.query('plan=="surf"')[['duration_calls','month']] 

mean_duration_calls_ultimate = mean_calls.query('plan=="ultimate"')[['duration_calls','month']].reset_index()

mean_duration_calls_surf

mean_duration_calls_ultimate





from matplotlib import pyplot as plt

fusion_final.pivot_table(index='month',columns='plan',values='duration_calls').plot(kind='bar')


# In[55]:


# Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.
sns.histplot(data = fusion_final, x='duration_calls', hue='plan')

plt.title('Monthly minutes used by plan')
plt.xlabel('Minutes')


# In[56]:


# Calcula la media y la varianza de la duración mensual de llamadas.

media = fusion_final.groupby('month')['duration_calls'].mean()

print(f"La media de la duración de llamadas es: {media}")

var_calls = fusion_final.groupby('month')['duration_calls'].var()
 
print(f"La varianza de la duración mensual de llamadas es: {var_calls}")



# In[57]:


mediana_calls = fusion_final.groupby('month')['duration_calls'].median() #Calcula mediana

mediana_calls


# In[58]:


desv_std_calls = fusion_final['duration_calls'].std #Calcula desviación estandar

desv_std_calls


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta muy bien pero explora mas estadisticos. La mediana, moda, la desviacion standard</div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>
# 

# In[59]:


# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas
plt.figure(figsize=(10, 6))

plt.boxplot(mean_duration_calls_surf['duration_calls'], positions=[1], widths=0.6, patch_artist=True, boxprops=dict(facecolor='orange', alpha=0.7), medianprops=dict(color='black'))

plt.boxplot(mean_duration_calls_ultimate['duration_calls'], positions=[2], widths=0.6, patch_artist=True, boxprops=dict(facecolor='green', alpha=0.7), medianprops=dict(color='black'))

plt.xticks([1, 2], ['surf', 'ultimate'])
plt.xlabel('Plan')
plt.ylabel('Duration Calls')
plt.title('Monthly Minutes Usage (Planes Surf y Ultimate)')
plt.grid(True)
plt.show()


# Existe una variación con respecto a los mins por llamada según el plan de cada usuario, los que usan el plan Surf al parecer sacan mayor provecho de sus beneficios, esto genera que sobrepasen lo incluido, todo esto en comparación con los usuarios de Ultimate.

# ### Mensajes

# In[60]:


# Compara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan
sms_monthly_amount = fusion_final.groupby('month')['messages_used'].count()
sms_monthly_mean = fusion_final.groupby('month')['messages_used'].mean()

print(sms_monthly_amount)
print(sms_monthly_mean)

#Traza un gráfico de barras del uso de Mensajes
fusion_final.pivot_table(index='month',columns='plan',values='messages_used').plot(kind='bar')


# In[61]:


#Traza un histograma para el uso de Mensajes

sns.histplot(data = fusion_final, x='messages_used', hue='plan')

plt.title('Monthly messages used by plan')
plt.xlabel('Messages')


# In[62]:


# Calcula la media y la varianza del uso de mensajes mensual.



media_sms = fusion_final.groupby('month')['messages_used'].mean()

print(f"La media del uso de sms es: {media_sms}")

var_sms = fusion_final.groupby('month')['messages_used'].var()
 
print(f"La varianza del uso mensual de sms es: {var_sms}")


# In[63]:


mediana_sms = fusion_final.groupby('month')['messages_used'].median() #Calcula mediana

mediana_sms


# In[64]:


desv_std_sms = fusion_final['messages_used'].std #Calcula desviación estandar

desv_std_sms


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta muy bien pero explora mas estadisticos. La mediana, moda, la desviacion standard</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[65]:


mean_sms = fusion_final.groupby(['plan','month'])['messages_used'].mean().reset_index()

mean_sms_surf = mean_sms.query('plan=="surf"')[['messages_used','month']] 

mean_sms_ultimate = mean_sms.query('plan=="ultimate"')[['messages_used','month']].reset_index()

mean_sms_surf
mean_sms_ultimate


# In[66]:


# Traza un diagrama de caja para visualizar la distribución del consumo mensual de mensajes

plt.figure(figsize=(10, 6))

plt.boxplot(mean_sms_surf['messages_used'], positions=[1], widths=0.6, patch_artist=True, boxprops=dict(facecolor='orange', alpha=0.7), medianprops=dict(color='black'))

plt.boxplot(mean_sms_ultimate['messages_used'], positions=[2], widths=0.6, patch_artist=True, boxprops=dict(facecolor='green', alpha=0.7), medianprops=dict(color='black'))

plt.xticks([1, 2], ['surf', 'ultimate'])
plt.xlabel('Plan')
plt.ylabel('SMS consumption')
plt.title('Monthly SMS Usage (Surf & Ultimate Plans)')
plt.grid(True)
plt.show()


# In[67]:


# Compara la cantidad de tráfico de Internet consumido por usuarios por plan
mean_mbs = fusion_final.groupby(['plan','month'])['gb_used'].mean().reset_index()


mean_mbs_surf = mean_mbs.query('plan=="surf"')[['gb_used','month']] 

mean_mbs_ultimate = mean_mbs.query('plan=="ultimate"')[['gb_used','month']].reset_index()

mean_mbs_surf

mean_mbs_ultimate


# In[68]:


#Traza un histograma para el uso de Gbs

sns.histplot(data = fusion_final, y='gb_used', hue='plan')

plt.title('gbs used by plan')
plt.xlabel('Month')
plt.ylabel('gbs')


# Se observa una diferencia entre los usuarios de los 2 planes, los del Surf se pasan del límite de lo que se incluye, lo cual resulta en un cobro extra a su plan.

# ### Internet

# In[69]:


# Compara la cantidad de gbs que tienden a usar cada mes los usuarios de cada plan
gbs_monthly_amount = fusion_final.groupby('month')['gb_used'].count()
gbs_monthly_mean = fusion_final.groupby('month')['gb_used'].mean()

gbs_monthly_amount
gbs_monthly_mean

#Traza un gráfico de barras del uso de Mensajes
fusion_final.pivot_table(index='month',columns='plan',values='gb_used').plot(kind='bar')


# In[70]:


#Traza un histograma para el uso de gbs

sns.histplot(data = fusion_final, x='gb_used', hue='plan')

plt.title('Monthly gbs used by plan')
plt.xlabel('GBS')


# In[71]:


# Calcula la media y la varianza del uso de gbs mensual.



media_gbs = fusion_final.groupby('month')['gb_used'].mean()

print(f"La media del uso de sms es: {media_gbs}")

var_gbs = fusion_final.groupby('month')['gb_used'].var()
 
print(f"La varianza del uso mensual de sms es: {var_gbs}")


# In[72]:


mediana_gbs = fusion_final.groupby('month')['gb_used'].median() #Calcula mediana

mediana_gbs


# In[73]:


desv_std_gbs = fusion_final['gb_used'].std #Calcula desviación estandar

desv_std_gbs


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta muy bien pero explora mas estadisticos. La mediana, moda, la desviacion standard</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[74]:


mean_gbs = fusion_final.groupby(['plan','month'])['gb_used'].mean().reset_index()

mean_gbs_surf = mean_gbs.query('plan=="surf"')[['gb_used','month']] 

mean_gbs_ultimate = mean_gbs.query('plan=="ultimate"')[['gb_used','month']].reset_index()

mean_gbs_surf
mean_gbs_ultimate


# In[75]:


# Traza un diagrama de caja para visualizar la distribución del consumo mensual de gbs

plt.figure(figsize=(10, 6))

plt.boxplot(mean_gbs_surf['gb_used'], positions=[1], widths=0.6, patch_artist=True, boxprops=dict(facecolor='blue', alpha=0.7), medianprops=dict(color='black'))

plt.boxplot(mean_gbs_ultimate['gb_used'], positions=[2], widths=0.6, patch_artist=True, boxprops=dict(facecolor='purple', alpha=0.7), medianprops=dict(color='black'))

plt.xticks([1, 2], ['surf', 'ultimate'])
plt.xlabel('Plan')
plt.ylabel('Gbs consumption')
plt.title('Monthly Gbs Usage (Surf & Ultimate Plans)')
plt.grid(True)
plt.show()


# Se observa una diferencia entre los usuarios de los 2 planes, los del Surf se pasan del límite de lo que se incluye, lo cual resulta en un cobro extra a su plan. Por su parte los usuarios de Ultimate están utilizando inteligentemente lo que incluye su paquete, lo cual hace que no se pasen en el consumo y tengan una tarifa estable.

# <div class="alert alert-block alert-warning">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Podrias extenderte en el analisis para agregar valor. ¿Por que crees que estaria pasando eso?. </div>

# ## Ingreso

# In[76]:


#Calcular tarifas por plan, con los cargos extras.

def total_income(row):
    
    if row['plan'] == 'surf':
        total = 20
        if row['duration_calls'] > 500:
            total += 0.03 * (row['duration_calls'] - 500)
        if row['messages_used'] > 50:
            total += 0.03 * (row['messages_used'] - 50)
        if row['gb_used'] > 15:
            total += 10 * (row['gb_used'] - 15)
            
    else:
        
        total = 70
        if row['duration_calls'] > 3000:
            total += 0.01 * (row['duration_calls'] - 3000)
        if row['messages_used'] > 1000:
            total += 0.01 * (row['messages_used'] - 1000)
        if row['gb_used'] > 30:
            total += 7 * (row['gb_used'] - 30)
    
    row['total_income'] = total
    
    return row

def extra_income(row):
    if row['plan'] == 'surf':
        if row['total_income'] > 20:
            return row['total_income'] - 20
        else:
            return 0
    elif row['plan'] == 'ultimate':
        if row['total_income'] > 70:
            return row['total_income'] - 70
        else:
            return 0
    else:
        return 0
    


# In[77]:


total_df = fusion_final.apply(total_income,axis=1)
total_df['extra_income'] = total_df.apply(extra_income,axis=1)
total_df


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# La funcion esta excelente, como recomendacion lo haria antes de armar el dataset por una cuestion de orden y estructura.
# 
# Si bien recien en este momento la utilizas, estaria bueno que lo dejes arriba. (En la seccion de estudiar las condiciones del plan). ***Señor revisor, por ejemplo, está corrección no me la habías hecho antes, por eso no lo había corregido, ya había checado esto con mi tutor, y no le vió nada malo por hacer la función aquí!!!</div> 

# In[78]:


mean_extra_income = total_df.groupby(['plan','month'])['extra_income'].mean().reset_index()


mean_extra_surf = mean_extra_income.query('plan=="surf"')[['extra_income','month']] 

mean_extra_ultimate = mean_extra_income.query('plan=="ultimate"')[['extra_income','month']].reset_index()

mean_extra_surf

mean_extra_ultimate


# In[79]:


mediana_income = total_df.groupby('month')['extra_income'].median() #Calcula mediana

mediana_income


# In[80]:


desv_std_income = total_df['extra_income'].std #Calcula desviación estandar

desv_std_income


# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Esta muy bien pero explora mas estadisticos. La mediana, moda, la desviacion standard</div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido.</div>

# In[81]:


# Traza un diagrama de caja para visualizar la distribución del consumo mensual de gbs

plt.figure(figsize=(10, 6))

plt.boxplot(mean_extra_surf['extra_income'], positions=[1], widths=0.6, patch_artist=True, boxprops=dict(facecolor='blue', alpha=0.7), medianprops=dict(color='black'))

plt.boxplot(mean_extra_ultimate['extra_income'], positions=[2], widths=0.6, patch_artist=True, boxprops=dict(facecolor='purple', alpha=0.7), medianprops=dict(color='black'))

plt.xticks([1, 2], ['surf', 'ultimate'])
plt.xlabel('Plan')
plt.ylabel('Extra income by plan')
plt.title('Extra income (Surf & Ultimate Plans)')
plt.grid(True)
plt.show()


# In[82]:


total_df.pivot_table(index='minutes_included',columns='plan',values='total_income').plot(kind='bar')


# In[83]:


total_df.pivot_table(index='messages_included',columns='plan',values='total_income').plot(kind='bar')


# In[84]:


total_df.pivot_table(index='gb_per_month_included',columns='plan',values='total_income').plot(kind='bar')


# In[85]:


total_df.pivot_table(index = 'month', columns = 'plan', values = 'duration_calls').plot(kind ='bar', figsize =[10, 5]) #Crea lineplot de los minutos usados mensualmente en el año por plan 


sns.lineplot(data = total_df, x = 'month', y = 'duration_calls' , hue = 'plan')
plt.title('Monthly minutes used by plan')
plt.xlabel('Month')
plt.ylabel('Minutes')

plt.boxplot(total_df['duration_calls'])
plt.show()


# In[86]:


total_df.pivot_table(index = 'month', columns = 'plan', values = 'messages_used').plot(kind ='bar', figsize =[10, 5]) #Crea lineplot de los mensajes usados mensualmente en el año por plan 


sns.lineplot(data = total_df, x = 'month', y = 'messages_used' , hue = 'plan')
plt.title('Monthly msgs used by plan')
plt.xlabel('Month')
plt.ylabel('Messages used')

plt.boxplot(total_df['messages_used'])
plt.show()


# In[88]:


total_df.pivot_table(index = 'month', columns = 'plan', values = 'gb_used').plot(kind ='bar', figsize =[10, 5]) #Crea lineplot de los gbs usados mensualmente en el año por plan 


sns.lineplot(data = total_df, x = 'month', y = 'gb_used' , hue = 'plan')
plt.title('Monthly gbs used by plan')
plt.xlabel('Month')
plt.ylabel('Gbs used')

plt.boxplot(total_df['gb_used'])
plt.show()


# In[89]:


total_df.pivot_table(index = 'month', columns = 'plan', values = 'total_income').plot(kind ='bar', figsize =[10, 5]) #Crea lineplot de los ingresos por plan, mensualmente en el año 


sns.lineplot(data = total_df, x = 'month', y = 'total_income' , hue = 'plan')
plt.title('Monthly income by plan')
plt.xlabel('Month')
plt.ylabel('Income')

plt.boxplot(total_df['total_income'])
plt.show()


# Los usuarios del plan Surf llegan a pagar más que el plan Ultimate, debido a que se pasan de lo incluido, y los usuarios del plan Ultimate, pagan menos excedentes por pasarse de lo que se incluye en su plan.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Realiza un lineplot para observar la evolucion en el tiempo de cada plan en los minutos de llamadas, internet y mensajes, agregando sus ingresos.
# Podrias hacerlo en dos graficos paralelos uno con un plan y otro en el otro. Pero explora tu imaginacion y hace esa evolucion.</div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Jorge, se mantiene la correccion para este punto. Faltaria realizar un lineplot por cada seccion o uno donde se encuentren todas -con ambos planes- o dos donde se encuentren todas por un plan cada uno.</div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor #3</b> <a class="tocSkip"></a>
# 
# Jorge, la correccion aun queda pendiente. Deberias realizar los respectivos graficos de linea para aprobar este proyecto.
# 
# </div>

# ## Prueba las hipótesis estadísticas

# Hipótesis nula: Los ingresos promedio de usuarios de Surf son iguales a los ingresos promedio de los usuarios de Ultimate.
# 
# Hipótesis alternativa: Los ingresos promedio de usuarios de Surf son diferentes a los ingresos promedio de los usuarios de Ultimate.

# In[ ]:


# Prueba las hipótesis
ultimate_income = total_df[total_df['plan'] == 'ultimate']['extra_calls']
surf_income = total_df[total_df['plan'] == 'surf']['extra_calls']

ultimate_income_var = np.var(ultimate_income)
ultimate_income_var

surf_income_var = np.var(surf_income)
surf_income_var


# In[ ]:


if ultimate_income_var ==  surf_income_var:
    varianza = True
else:
    varianza = False
    
print("El valor de la varianza es: ", varianza)


# In[ ]:


alpha = 0.05

results = st.ttest_ind(ultimate_income,surf_income)


# In[ ]:


# Prueba las hipótesis
print('valor p:', results.pvalue)

if results.pvalue < alpha:
    print("Rechazamos la hipotesis nula")
else:
    print("No podemos rechazar la hipotesis nula")


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor </b> <a class="tocSkip"></a>
# 
# Cuando realizamos la prueba de t.estudent es muy importante un parametro que es el equal_var (False or True), que significa si existe la igualdad de varianzas o no de ambas muestras. En este trabajo no pedimos ser finos con esto pero te lo dejo a modo de que entiendas el porque y te va a servir en futuros proyecto. 
# 
# El objetivo de la prueba de t de Student es comparar las medias de dos grupos de datos y determinar si existen diferencias significativas entre ellos. Se aplica cuando estamos interesados en saber si la diferencia entre las medias es real o simplemente producto del azar.
# 
# Para esto generamos dos hipotesis H0 y H1 (nula y alternativa, respectivamente).
# 
# Hipótesis nula (H0): No hay diferencia significativa entre las medias de los dos grupos.
# Hipótesis alternativa (H1): Hay una diferencia significativa entre las medias de los dos grupos.
# 
# En este caso **realizas una observacion de las dos varianzas**, lo que no esta mal, pero depender únicamente de la diferencia en los valores de las varianzas puede llevar a conclusiones equivocas, mas que nada si las muestras tienen tamaños diferentes . Las pruebas estadísticas están diseñadas para tomar en cuenta el tamaño de la muestra y calcular si la diferencia observada en las varianzas es estadísticamente significativa o si podría deberse al azar.
# 
# Para saber lo del equal_var utilizamos La función levene en scipy.stats que se utiliza para realizar una prueba de igualdad de varianzas entre dos grupos de datos. (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levene.html)
# 
# Los resultados  de esta prueba es muy parecido a lo que hacemos en el t.student. Ya que Si el valor p obtenido en la prueba levene es mayor que un nivel de significancia (alpha) previamente elegido (por ejemplo, 0.05), entonces asumimos que las varianzas son iguales (aceptamos H0).
# Si el valor p es menor que alpha, rechazamos la hipótesis nula y asumimos que las varianzas son diferentes.
# 
# Por lo tanto, si las varianzas son iguales (aceptamos H0 en la prueba levene), puedes establecer equal_var=True al realizar la prueba t de Student.
# Si las varianzas son diferentes (rechazamos H0 en la prueba levene), debes establecer equal_var=False al realizar la prueba t de Student. Esto indica que se debe usar una versión de la prueba t que no asuma igualdad de varianzas, como la prueba Welch's t.
# 
# Siempre recordar que los outliers pueden impactar negativamente en esta prueba (t.student)
# 
# Esto es basicamente por lo que te corrijo lo del equal_var pero es como consejo y que lo sepas a futuro. Esta en vos si lo queres modificar o no.
# 
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Corregido. Excelente, Jorge. Si bien estas observando las varianzas para ambos en general preferimos una prueba estadistica que evalue si la varianza es tal, ya que una simple observacion a veces no es suficiente.</div>

# Hipótesis nula: Los ingresos promedio de usuarios de NY-NJ son iguales a los ingresos promedio de los usuarios de otras regiones.
# Hipótesis alternativa: Los ingresos promedio de usuarios de NY-NJ son diferentes a los ingresos promedio de los usuarios de otras regiones.    
# 

# In[ ]:


nynj_income = total_df[total_df['city'] == 'New York-Newark-Jersey City, NY-NJ-PA MSA']['extra_calls']
other_city =  total_df[total_df['city'] != 'New York-Newark-Jersey City, NY-NJ-PA MSA']['extra_calls']

nynj_income_var = np.var(nynj_income)

other_city_var = np.var(other_city)



# In[ ]:


if nynj_income_var ==  other_city_var:
    varianza = True
else:
    varianza = False
    
print("El valor de la varianza es: ", varianza)


# In[ ]:


alpha = 0.05

results = st.ttest_ind(nynj_income, other_city, equal_var = varianza)



print('valor p:', results.pvalue)

if results.pvalue < alpha:
    print("Rechazamos la hipotesis nula")
else:
    print("No podemos rechazar la hipotesis nula")


# Conclusiones:
# 
# - El objetivo central del proyecto es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.
# - El proyecto ha comenzado en el paso 2.1, mediante la importación de las diferentes bibliotecas que se emplearon para su desarrollo.
# - Enseguida se cargaron los datos de las 5 respectivas tablas, además se nombraron estas de acuerdo a su concepto: megacalls_df, internet_df, msn_df, plans_df y users_df.
# - Después en la sección 2.3 se prepararon los datos de las 5 tablas mediante la impresión de la información resumida de los dataframes mediante .info(), .describe(), .head(5), etc.
# - En la sección 2.5 se corrigieron los datos mediante la revisión de valores duplicados, búsqueda de valores ausentes, etc. También se convirtió la columna de mb_per_month_included a gbs, con el objetivo de medir todo en base a 'gbs' como lo dicen los planes.
# - Se enriquecieron los datos al quitar la columna mb_per_month_included que ya no sería usada.
# - Pasamos a la parte 2.7 en donde se trabajó con la tabla de usuarios; users_df, en la cual se corrigieron algunos datos como transformar las columnas churn_date y reg_date a tipo de dato datetime, para poder llevar a cabo cálculos númericos con otras columnas.
# - Sección 2.8 para el df de llamadas; megacalls_df, se convirtió la columna call_date a tipo datetime. se redondearon los datos de la columna duration al siguiente número entero, ya que asi se manejan las tarifas. Se cambió el nombre de la columna id a id_call y se cambió el dato a tipo entero, para poder relacionarlo con otras columnas con el mismo tipo de datos. Esta columna será vital en el proyecto, ya que ayudará a relacionar información entre las diferentes tablas. Parte 2.8.2 se extrajó el número de mes de la columna call_date y se cambió el nombre de esta a 'month', ya que la mayoría de los cálculos posteriores serán por mes. 
# - Parte 2.9 se trata sobre la tabla correspondiente a Mensajes; msn_df, se convierte la columna message_date a tipo datetime, se renombra la columna "id" a "id_message", además se cambia la columna id_message, a tipo de dato entero. También en esta tabla se va a extraer el número de mes de la columna message_date, y esta se cambia al nomnre de month.
# - La sección 2.10 corresponde a la tabla de Internet; internet_df, en la cual se corrigieron datos como la transformación de la columna session_date a tipo datetime, se renombra aquí también la columna "id" a  "id_internet" y se transforma a tipo entero, con el objetivo de facilitar la relación entre las tablas. Igual que con las otras tablas, se extrae el número de mes de la columna session_date y se renombra month. Viene una parte importante del proyecto donde se hace un código para transformar la medición de los datos de internet consumidos, se cambia mb_used a gb_used; es decír mbs por gbs, ya que la forma en la que se cobra el internet en la compañia, es por medio de los gbs consumidos por el usuario.
# - A continuación en la parte 2.11, se estudiarán las condiciones de las tarifas. Se calculan la cantidad de llamadas hechas durante el mes por usuario, el resultado se guarda en una nueva columna llamada calls_made, se ejecutan otros cálculos como la cantidad de minutos usados por cada usuario al mes, se calcula el número de mensajes enviados por cada usuario al mes, también el volumen de tráfico de Internet usado por cada usuario al mes. 
# - Enseguida se hace una nueva tabla mediante la fusión de los cálculos mensuales de consumo de llamadas, mensajes y gbs, con base en las columnas que tienen en común; user_id y month, se le llama a dicha tabla 'fusion_data' que tiene las siguientes columnas: user_id, month, calls_made, duration_calls, messages_used y gb_used.
# - Se hace otro dataframe llamado fusion_data_plus_users en donde se hace un merge de la tabla fusion_data con algunas columnas del df users_df: 'user_id','city','plan'.
# - Finalmente se crea el df fusion_final, en donde se hace un merge de la tabla fusion_data_plus_users con plans_df, y se cambia la columna plan_name a plan, para tener el mismo nombre en los distintos dataframes.
# - La tabla fusion_final queda con 14 columnas, todas de tipo numerico: 
#  
# ---  ------                 --------------  -----  
#  0   user_id                2293 non-null   int64  
#  1   month                  2293 non-null   int64  
#  2   calls_made             2293 non-null   float64
#  3   duration_calls         2293 non-null   float64
#  4   messages_used          2293 non-null   float64
#  5   gb_used                2293 non-null   float64
#  6   city                   2293 non-null   object 
#  7   plan                   2293 non-null   object 
#  8   messages_included      2293 non-null   int64  
#  9   minutes_included       2293 non-null   int64  
#  10  usd_monthly_pay        2293 non-null   int64  
#  11  usd_per_gb             2293 non-null   int64  
#  12  usd_per_message        2293 non-null   float64
#  13  usd_per_minute         2293 non-null   float64
#  14  gb_per_month_included  2293 non-null   float64
# dtypes: float64(7), int64(6), object(2)
# memory usage: 286.6+ KB
# 
# - A continuación se hace un np.ceil a la columna gb_used para redondear el uso de gbs, de acuerdo a como lo indican las tarifas. En la parte 2.12 ya se estudia el comportamiento de usuario, primero en la parte 2.12.1 de llamadas, se compara la duración promedio de llamadas por cada plan y por cada mes y se traza un gráfico de barras para observarlo. Enseguida se compara el número de minutos mensuales que necesitan los usuarios de cada plan y se traza un histograma. También se calcula la media, varianza, mediana y desviación estandár para la duración mensual de llamadas. Además se traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas.
# - Después se pasa a los calculos de mensajes, se compara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan y se traza un gráfico de barras para observarlo. Enseguida se compara el número de mensajes mensuales que necesitan los usuarios de cada plan y se traza un histograma. También se calcula la media, varianza, mediana y desviación estandár para el uso de mensajes mensual. Además se traza un diagrama de caja para visualizar la distribución del consumo mensual de mensajes.
# - Después se pasa a los calculos de uso de internet, se compara la cantidad de tráfico de Internet consumido por usuarios por plan . Enseguida se compara el número de gbs mensuales que necesitan los usuarios de cada plan y se traza un histograma. También se calcula la media, varianza, mediana y desviación estandár para el uso de gbs mensual. Además se traza un diagrama de caja para visualizar la distribución del consumo mensual de gbs.
# - Sección 2.13, se tratan los datos de ingresos de los usuarios por plan, primero se calculan las tarifas por plan, tomando en cuenta los cargos extras, con esto se genera un nuevo df llamado total_df, en donde se le hace un apply a la tabla fusion_final para agregar la columna extra_income, se hace un calculo de la media de ingresos mensuales extras por plan, además de otras estadísticas como la mediana, desviación estandár y se traza un diagrama de caja para visualizar la distribución del consumo mensual de gbs potr plan y con el ingreso extra. Se trazan otros gráficos para visualizar la evolución en el tiempo de cada plan y sus ingresos, por llamadas, internet y mensajes. 
# - Acontinuacipon pasamos a la sección 2.14 donde se tratan las hipótesis. Los usuarios del plan Surf tienden a gastar más en su plan debido a que se pasan de que se incluye en el plan.
# - De acuerdo al tratamiento de las 2 hipótesis, se rechazó la H nula debido a que los ingresos promedio de usuarios de Surf son diferentes a los ingresos promedio de los usuarios de Ultimate, así como se planteó en la H alternativa. Y en cuanto a la hipótesis de la comparación entre las ciudades, se probó que los ingresos promedio de usuarios de NY-NJ son iguales a los ingresos promedio de los usuarios de otras regiones, probando la H nula.
# - Se observó que ambos plantes tienen un consumo similar de los diferentes medios, tal vez a la mayoría de los usuarios les conviene cambiar a Ultimate.
# - Usuarios de Ultimate aprovechan su plan mejor que los de Surf, ya que los primeros se pasan menos del consumo de lo que se incluye en su plan.
# - Se deberá recomendar a llevar a cabo una campaña de marketing, enfocada en motivar a los usuarios de Surf a subir su plan a Ultimate, de esta forma estarían pagando menos por excederse en el uso de su plan.
# - Antes de llevar la fusión de tabalas, se tuvieron que cambiar el tipo de datos y renombrar columnas, todo esto basado sobre los nombres 'month' y 'user_id', además fue determinante cambiar los megas a gb. Una vez preparados correctamente los datos, se hizo un poco más simple el calculo estadístico de los datos. Se crea el df fusion_data_plus_users para fusionar las tablas de fusion_data con la de users_df, enseguida se crea otra tabla llamada fusion_final para juntar el df fusion_data_plus_users con plans_df, en donde la columna plan_name se cambia a plan.

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Recorda realizar una conclusion general. Esta debe contener todo lo que se hizo en el proyecto de forma enumerada o items.
# 
# Desde la carga e importacion, pasando por los cambios realizado (Y el porque de esas decisiones). Agregando lo que se hizo en cada seccion a modo resumen y las conclusiones del  trabajo.
# 
# Sirve como resumen de lo realizado en cada proyecto.</div>
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
# 
# Jorge, hiciste una conclusion general excelente. Me encanto leer tantos detalles y explicaciones claras y concisas. Te felicito.</div>

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario general #1</b> <a class="tocSkip"></a>
# 
# Jorge, has realizado un muy buen trabajo. Entendiste que se buscaba en cada paso y actuast en consecuencia.
# 
# Valoro mucho como trataste los datos y como estuviste en los detalles de cada cosa. 
# 
# A nivel codigo esta excelente como planteas cada caso, en cuanto al analisis son muy buenos pero como consejo, aprovecha lo bueno que son para extenderte un poco mas y agregar mayor valor.
# 
# En general esta muy bien y restan detalles o consejos. 
# 
# Espero tu correccion, saludos.</div>

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario general #2</b> <a class="tocSkip"></a>
# 
# Jorge,  tus correcciones fueron impecables. Todas las que encaraste fueron muy bien realizaste y tu proyecto practicacmente esta hecho, muy bien.
# 
# Te pido disculpas nuevamente por mi error en la correccion del punto del paso de mb a gb.
# 
# Resta una correccion que es la de los lineplots, con eso el trabajo estara aprobado.
# Te deje un comentario sobre los ingresos para tenerlo en cuenta, y tambien a la hora de observar las varianzas.
# 
# 
# Te felicito de nuevo por tus conclusiones generales que me encanto leer.
# 
# Quedo atento a tu correccion, saludos.</div>
# 
# 
# 
# 

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario general #3</b> <a class="tocSkip"></a>
# 
# Jorge, aun resta el punto de crear los lineplots. Como te dije en ese punt ose espera que tanto **internet, mensajes, llamadas, usuarios e ingresos** tengan una evolucion en el tiempo en los consumos.
# 
# Con eso, como te dije en el comentario anterior, estara aprobado el proyecto.
#     
# Con respecto a lo que escribiste, lamento que creas que haya algo en contra de la aprobacion de este  bueno trabajo. No es asi y tampoco quiero que lo sientas, como te digo el comentario de los lineplots estaban ahi desde la iteracion #1 y lamento si no fui claro al respecto para que entiendas que se buscaba.
#     
# A su vez, el unico comentario nuevo generado fue el de los ingresos y como te dije es una recomendacion y no una correccion en la cual se necesite un cambio. Cuando creamos un dataset nuevo de uniones, siempre esta bueno a nivel estructura que dejes definido el dataset final para luego hacer lo que quieras, ya que de esta forma si hay un error seria mucho mas facil corregirlo y encontrarlo.
# Como te digo no es que fueron muchisimos y al percatarme lo deje no como para marcar algo malo sino que si yo estiviera en tu situacion de alumno me hubiera gustado que me lo hagan saber.
#     
# Como te digo, haciendo el lineplot el trabajo estara aprobado.
#     
# Saludos.
#     
#     
#     
# </div>

# In[ ]:




