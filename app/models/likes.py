from sqlalchemy import Integer


class Like(db.Model):
    __tablename__ = 'like'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('post.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Like(id={self.id} user_id={self.user_id} post_id={self.post_id})"