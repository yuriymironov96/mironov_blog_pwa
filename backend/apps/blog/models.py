import datetime

from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from apps.core.database import Base


class Tag(Base):
    __tablename__ = 'blog_article'

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    title = Column(
        Text,
        nullable=False
    )


class Entry(Base):
    '''
    Either blog article or its comment.
    '''
    __tablename__ = 'blog_entry'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    title = Column(
        Text,
        nullable=False
    )
    text = Column(
        Text,
        nullable=False
    )
    create_time = Column(
        DateTime,
        default=datetime.datetime.now
    )
    update_time = Column(
        DateTime,
        onupdate=datetime.datetime.now
    )
    parent_id = Column(
        Integer,
        ForeignKey('blog_entry.id')
    )
    children = relationship(
        'blog_entry',
        backref=backref('parent', remote_side=[id])
    )
