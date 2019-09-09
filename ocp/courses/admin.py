from django.contrib import admin
from .models import Category, Course, Enrollment, Announcement, Comment, Lesson, Material, Teacher
from .forms import MaterialForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

    # def has_add_permission(self, request): ????
    #     if Category.slug.count() == 1:
    #         return False
    #     return True
    #
    # def has_delete_permission(self, request, obj=None): ???????????
    #     return False

class TeacherInCourse(admin.TabularInline):
    model = Teacher.course.through
    #extra = 3 ???? verificar onde pode ser usado


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'phone', 'url', 'start_date', 'image', 'hascertification', 'status')
    search_fields = ['name', 'slug',]
    #gera vinculo de professor ao curso
    incourses = [TeacherInCourse,]

    # def show_categories(self, obj): ???
    #     return "\n; ".join([cat.title for cat in obj.category.all()])

    # def get_queryset(self, request): ???
    #     return super().get_queryset(request).prefetch_related('categories')


class TeacherAdmin(admin.ModelAdmin):
    # campo da tabela Teacher que será usado como filtro
    filter_horizontal = ("course",)
    incourses = [TeacherInCourse,]


class MaterialInLessonAdmin(admin.StackedInline):
    model = Material


class MaterialAdmin(admin.ModelAdmin):
    form = MaterialForm
    model = Material


class LessonAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'updated_at', )
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    inlesson = [MaterialInLessonAdmin]


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register([Enrollment, Announcement, Comment])
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Material, MaterialAdmin)