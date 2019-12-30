from django.db import models

# Create your models here.

class TodoList(models.Model):
    no = models.AutoField(auto_created = True, verbose_name ='ID', primary_key=True)
    pcode = models.CharField(verbose_name='PCODE', max_length=4)
    # user_id = models.CharField(verbose_name='USER_ID', max_length=50, blank=True, null=True)
    title = models.CharField(verbose_name='TITLE', max_length=200, blank=True, null=True)
    content = models.CharField(verbose_name='CONTENT', max_length=1000, blank=True, null=True)
    is_complete = models.IntegerField(verbose_name='IS_COMPLETE', blank=True, null=True)
    priority = models.IntegerField(verbose_name='PRIORITY', blank=True, null=True)
    end_date = models.DateField(verbose_name='END_DATE', blank=True, null=True)
    
    class Meta:
        # verbose_name = '할일'
        # verbose_name_plural = '할일 모음'
        ordering = ['title', ]

    def __str__(self):
        return self.title
    
    def todo_save(self):
        #저장 버튼을 누르면 바로 저장을 하지 않고 todo_save 함수를 호출하면 저장되도록
        # save 하기 전에 default로 db값을 넣어주도록 하기위해서
        # is_complete는 1이 아닌 0의 값을 가져야 하기 때문에
        self.save() 