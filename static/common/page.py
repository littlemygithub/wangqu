
class PagerHelper:
    def __init__(self,total_count,current_page,base_url,per_page=10):
        self.total_count = total_count
        self.current_page = current_page
        self.base_url = base_url
        self.per_page = per_page
    @property
    def db_start(self):
        return (self.current_page-1) * self.per_page

    @property
    def db_end(self):
        return (self.current_page)*self.per_page

    def total_page(self):
        v, a = divmod(self.total_count, self.per_page)
        if a != 0:
            v += 1
        return v
    def pager_str(self):
        v = self.total_page()
        pager_list = []
        if self.current_page == 1:
            pager_list.append('<li><a href="#">&laquo;</a></li>')
        else:
            pager_list.append('<li><a href="%s?p=%s">&laquo;</a></li>' % (self.base_url,self.current_page - 1))
        if v <= 11:
            page_range_start = 1
            page_range_end = v + 1
        else:
            if self.current_page < 3:
                page_range_start = 1
                page_range_end = 6 + 1
            else:
                page_range_start = self.current_page - 2
                page_range_end = self.current_page + 2 + 1
                if page_range_end > v:
                    page_range_start = v - 4
                    page_range_end = v + 1

        for i in range(page_range_start, page_range_end):
            if i == self.current_page:
                pager_list.append('<li><a class="active" href="%s?p=%s">%s</a></li>' % (self.base_url ,i, i))
            else:
                pager_list.append('<li><a href="%s?p=%s">%s</a></li>' % (self.base_url,i, i))

        if self.current_page == v:
            pager_list.append('<li><a href="#">&raquo;</a></li>')
        else:
            pager_list.append('<li><a href="%s?p=%s">&raquo;</a></li>' % (self.base_url ,self.current_page + 1))
        pager = "".join(pager_list)
        return pager