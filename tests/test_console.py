#!/usr/bin/python3
"""Test for the console"""

import sys
sys.path.append('..')
import unittest
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up for the test"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down after the test"""
        sys.stdout = self.backup
        self.capt_out.close()
        del self.console

    def test_quit(self):
        """Test quit command"""
        self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        """Test create command"""
        self.console.onecmd("create BaseModel")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_show(self):
        """Test show command"""
        new_instance = BaseModel()
        new_instance.save()
        object_id = new_instance.id

        self.capt_out = StringIO()
        sys.stdout = self.capt_out

        self.console.onecmd("show BaseModel " + object_id)
        output = self.capt_out.getvalue()
        self.assertTrue(isinstance(output, str))

    def test_show_class_name_missing(self):
        """Test show command with missing class name"""
        self.console.onecmd("show")
        output = self.capt_out.getvalue()
        self.assertEqual("** class name missing **\n", output)

    def test_show_instance_id_missing(self):
        """Test show command with missing instance id"""
        self.console.onecmd("show BaseModel")
        output = self.capt_out.getvalue()
        self.assertEqual("** instance id missing **\n", output)

    def test_show_no_instance_found(self):
        """Test show command with non-existent instance"""
        self.console.onecmd("show BaseModel 123456")
        output = self.capt_out.getvalue()
        self.assertEqual("** no instance found **\n", output)

    def test_create_class_name_missing(self):
        """Test create command with missing class name"""
        self.console.onecmd("create")
        output = self.capt_out.getvalue()
        self.assertEqual("** class name missing **\n", output)

    def test_create_class_name_doesnt_exist(self):
        """Test create command with non-existent class name"""
        self.console.onecmd("create Binita")
        output = self.capt_out.getvalue()
        self.assertEqual("** class doesn't exist **\n", output)

if __name__ == '__main__':
    unittest.main()

