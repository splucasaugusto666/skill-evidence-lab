import unittest,tempfile,shutil,json
from pathlib import Path
import skilllab as s
class TestLab(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup); self.root=Path(self.tmp.name); self.lib=self.root/'lib'; shutil.copytree(s.ROOT/'skills',self.lib);self.ws=self.root/'work';self.ws.mkdir();self.name='code-review';self.src=self.lib/self.name
    def test_catalog(self): self.assertEqual(len(s.catalog(self.lib)),12)
    def test_catalog_snapshot(self): self.assertEqual(s.catalog(self.lib),s.read_json(s.ROOT/'catalog.json'))
    def test_dry_run(self): self.assertFalse(s.install(self.lib,self.name,self.ws,'codex',True).exists());self.assertEqual(list(self.ws.iterdir()),[])
    def test_install_all_targets(self):
        for platform in s.PLATFORMS:
            with self.subTest(platform=platform): self.assertEqual(s.validate(s.install(self.lib,self.name,self.ws,platform)),s.validate(self.src))
    def test_no_overwrite(self):
        p=s.install(self.lib,self.name,self.ws,'manual')
        with self.assertRaises(ValueError): s.install(self.lib,self.name,self.ws,'manual')
        self.assertEqual(s.validate(p),s.validate(self.src))
    def test_tamper(self):
        with (self.src/'SKILL.md').open('a') as f: f.write('tampered')
        with self.assertRaisesRegex(ValueError,'checksum'): s.validate(self.src)
    def test_extra_script(self):
        (self.src/'run.sh').write_text('echo never run')
        with self.assertRaises(ValueError): s.validate(self.src)
    def test_traversal(self):
        with self.assertRaises(ValueError): s.install(self.lib,'../outside',self.ws,'manual')
    def test_symlink_source(self):
        p=self.lib/'alias'
        try: p.symlink_to(self.src,target_is_directory=True)
        except OSError: self.skipTest('symlinks unavailable')
        with self.assertRaises(ValueError): s.validate(p)
    def test_symlink_destination(self):
        outside=self.root/'outside';outside.mkdir()
        try: (self.ws/'.agents').symlink_to(outside,target_is_directory=True)
        except OSError: self.skipTest('symlinks unavailable')
        with self.assertRaises(ValueError): s.install(self.lib,self.name,self.ws,'codex')
        self.assertEqual(list(outside.iterdir()),[])
    def test_duplicate_manifest_keys(self):
        p=self.src/'manifest.json';p.write_text('{"name":"a","name":"b"}')
        with self.assertRaisesRegex(ValueError,'duplicate'): s.validate(self.src)
    def test_unknown_permission(self):
        p=self.src/'manifest.json';m=json.loads(p.read_text());m['permissions']['execution']='arbitrary';p.write_text(json.dumps(m))
        with self.assertRaises(ValueError): s.validate(self.src)
    def test_missing_skill(self):
        with self.assertRaises(ValueError): s.install(self.lib,'missing',self.ws,'manual')
    def test_manifest_name_mismatch(self):
        p=self.src/'manifest.json';m=json.loads(p.read_text());m['name']='another';p.write_text(json.dumps(m))
        with self.assertRaises(ValueError): s.validate(self.src)
    def test_empty_library(self):
        p=self.root/'empty';p.mkdir()
        with self.assertRaises(ValueError): s.catalog(p)
if __name__=='__main__': unittest.main()
