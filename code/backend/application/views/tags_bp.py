
# - Creating tags
# - getting tags 
# - update tags 
# - delete tags 


from flask import Blueprint, request
from flask_restful import Api, Resource
from application.logger import logger
import hashlib
import time
from application.database import db
from application.common_utils import (
    token_required,
    users_required,
)
from application.common_utils import (
    convert_base64_to_img,
    convert_img_to_base64,
    is_img_path_valid,
    is_base64,
    get_encoded_file_details,
)
from application.views.user_utils import UserUtils,time_to_str
from application.responses import *
from application.globals import *
from application.models import *
from copy import deepcopy
from application.notifications import send_email


class TagsUtil(UserUtils): 
    def convert_tags_to_dict(self, tags): 
        tags_dict = vars(tags)  # verify if this properly converts obj to dict
        if "_sa_instance_state" in tags_dict:
            del tags_dict["_sa_instance_state"]
        
        return tags_dict
    
tags_bp = Blueprint("tags_bp", __name__)
tags_api = Api(tags_bp)
tags_util = TagsUtil()

class TagsAPI(Resource): 

    def get(self): 
    #this method is used to get all of the available tags
        try:
            all_tags = []
            tags = Tags.query.all() 
            for tag in tags: 
                t = tags_util.convert_tags_to_dict(tag)
                all_tags.append(t)
            logger.info(f"All tags found!")
            return success_200_custom(data=all_tags)
        except Exception as e:
            logger.error(f"TagsAPI->get : Error occured while fetching FAQ data : {e}")
            raise InternalServerError

    #how are tags added? 
    def post(self): 
        return ""
    
    #is there a need to update/edit the tags? 
    def put(self): 
        return ""
    
    def delete(self): 
        return ""