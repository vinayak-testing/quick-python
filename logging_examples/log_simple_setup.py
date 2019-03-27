"""Simple logging setup"""
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

logger.info("This is my first logging : %s", 'Vinayak')
