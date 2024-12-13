[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wGJQJZMO)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17529069&assignment_repo_type=AssignmentRepo)
#### **Título: Sistema de Gestión de Cursos y Estudiantes**

Desarrolla una aplicación en Django para gestionar cursos y estudiantes. La aplicación debe incluir modelos relacionados a través de una entidad intermedia, formularios con validaciones personalizadas usando el método `clean`, y vistas para gestionar los datos.

---

### **Especificaciones**

#### **1. Modelos**

Crea los siguientes modelos en `models.py`:

1. **Curso**:
   - `nombre`: Cadena de texto (máximo 100 caracteres).
   - `codigo`: Código único del curso (máximo 10 caracteres).
   - `fecha_inicio`: Fecha de inicio del curso.
   - `fecha_fin`: Fecha de finalización del curso.

   **Restricción**: La fecha de inicio debe ser anterior a la fecha de finalización.

2. **Estudiante**:
   - `nombre`: Cadena de texto (máximo 100 caracteres).
   - `email`: Correo electrónico único.
   - `fecha_nacimiento`: Fecha de nacimiento.

   **Restricción**: La fecha de nacimiento no debe ser posterior al día actual, y el estudiante debe tener al menos 18 años.

3. **Inscripción**:
   - `estudiante`: Relación de muchos a uno con el modelo **Estudiante**.
   - `curso`: Relación de muchos a uno con el modelo **Curso**.
   - `fecha_inscripcion`: Fecha de inscripción.

   **Restricción**: 
   - Un estudiante no puede inscribirse en un curso que ya haya finalizado.
   - La fecha de inscripción no puede ser posterior al día actual.
---

#### **2. Formularios**

Crea formularios en `forms.py` para gestionar los datos de los modelos. Incluye las siguientes validaciones personalizadas usando el método `clean`:

1. En el formulario de creación de un **Curso**, valida que:
   - La fecha de inicio sea anterior a la fecha de finalización.

2. En el formulario de creación de un **Estudiante**, valida que:
   - El correo electrónico sea único.
   - El estudiante tenga al menos 18 años (basado en la fecha de nacimiento).

3. En el formulario de **Inscripción**, valida que:
   - El curso al que se inscribe no haya finalizado (comparando la fecha de inscripción con la fecha de finalización del curso).
   - No permita inscribir a un estudiante en el mismo curso más de una vez.

---

#### **3. Vistas**

Crea vistas basadas en funciones para:

1. **Cursos**:
   - Crear un nuevo curso.
   - Listar todos los cursos.
   - Editar un curso existente.
   - Eliminar un curso.

2. **Estudiantes**:
   - Crear un nuevo estudiante.
   - Listar todos los estudiantes.
   - Editar la información de un estudiante.
   - Eliminar un estudiante.

3. **Inscripciones**:
   - Crear una nueva inscripción.
   - Listar todas las inscripciones.
   - Eliminar una inscripción.

---

#### **4. Plantillas**

Crea plantillas HTML para mostrar los formularios y los datos de cada modelo. Asegúrate de:

1. Mostrar los errores de validación cuando un formulario sea inválido.
2. Crear una página principal que enlace a las vistas de cursos, estudiantes e inscripciones.

---

### **Pistas**

1. **Validaciones Personalizadas**:
   - Usa el método `clean()` o `clean_<campo>()` en los formularios para implementar las restricciones.

   Ejemplo en `InscripcionForm`:
   ```python
   def clean(self):
       cleaned_data = super().clean()
       fecha_inscripcion = cleaned_data.get('fecha_inscripcion')
       curso = cleaned_data.get('curso')

       if fecha_inscripcion > curso.fecha_fin:
           raise forms.ValidationError("No se puede inscribir a un curso que ya ha finalizado.")
   ```

2. **Relaciones**:
   - Usa `ForeignKey` en **Inscripción** para conectar estudiantes y cursos.

3. **CSRF Protection**:
   - No olvides incluir `{% csrf_token %}` en los formularios de las plantillas.

4. **Redirección**:
   - Redirige al usuario a una lista tras completar la creación o edición de un elemento.
